"""
@File : operations.py
@Author: Dong Wang
@Date : 2020/4/1
@Description : Implement of an operation vertex of the computational graph
"""
from . import DEFAULT_GRAPH
from . import backend
from . import Node


class Operation(Node):
    """This is an abstract class for operations
        each subclass should implement compute_output and compute_gradient
    """

    def __init__(self, *input_nodes):
        """ Operation constructor.
        :param input_nodes: Input nodes for this operation.
        :type input_nodes: variables,placeholders.
        """

        super(Operation, self).__init__()  # PEP 3135
        # Check the type of input_nodes
        for node in input_nodes:
            assert isinstance(node, Node), "Wrong type, input_nodes can only be Variable, Operation, Placeholder"

        # nodes for operation
        self.input_nodes = input_nodes
        # nodes for recursive
        self.output_nodes = []
        # Output value of specified operation for input_nodes
        self.output_value = None

        self.graph = DEFAULT_GRAPH

        for node in input_nodes:
            node.output_nodes.append(self)
        # Add this operation to default graph.
        self.graph.operations.append(self)

    def compute_output(self):
        raise NotImplementedError

    def compute_gradient(self):
        raise NotImplementedError


class Add(Operation):
    """ An addition operation.
    """

    def __init__(self, x, y):
        """ Addition constructor.
        :param x: The first input node.
        :type x: Object of `Operation`, `Variable` or `Placeholder`.
        :param y: The second input node.
        :type y: Object of `Operation`, `Variable` or `Placeholder`.
        """
        super(Add, self).__init__(x, y)

    def compute_output(self):
        """ Compute and return the value of addition operation.
        """
        x, y = self.input_nodes
        self.output_value = backend.add(x.output_value, y.output_value)
        return self.output_value

    def compute_gradient(self):
        # TODO Add.compute_gradient
        pass


class Multiply(Operation):
    """ Multiplication operation.
    """

    def __init__(self, x, y, name=None):
        """ Multiplication constructor.
        :param x: The first input node.
        :type x: Object of `Operation`, `Variable` or `Placeholder`.
        :param y: The second input node.
        :type y: Object of `Operation`, `Variable` or `Placeholder`.
        """
        super(Multiply, self).__init__(x, y)

    def compute_output(self):
        """ Compute and return the multiplication operation result.
        """
        x, y = self.input_nodes
        self.output_value = backend.multiply(x.output_value, y.output_value)
        return self.output_value

    def compute_gradient(self):
        # TODO Multiply.compute_gradient
        pass


class MatMul(Operation):
    """ Matrix multiplication operation.
    """

    def __init__(self, x, y, name=None):
        """ MatMul constructor.
        :param x: The first input node.
        :type x: Object of `Operation`, `Variable` or `Placeholder`.
        :param y: The second input node.
        :type y: Object of `Operation`, `Variable` or `Placeholder`.
        """
        super(MatMul, self).__init__(x, y)

    def compute_output(self):
        """ Compute and return the multiplication operation result.
        """
        x, y = self.input_nodes
        self.output_value = backend.dot(x.output_value, y.output_value)
        return self.output_value

    def compute_gradient(self):
        # TODO MatMul.compute_gradient
        pass