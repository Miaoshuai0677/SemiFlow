"""
@File : test_losses.py
@Author: Dong Wang
@Date : 2020/6/8
"""
import numpy as np
from SemiFlow import losses
from SemiFlow.layer.input import InputLayer


def test_none():
    try:
        none = losses.get(None)
    except Exception as e:
        assert e.args[0] == 'You should specify a loss function'


def test_mse():
    fn = 'mse'
    y_pred = np.array([[1, 2], [3, 4]])
    y_true = np.zeros((2, 2))
    Loss = losses.get(fn)
    Input = InputLayer(shape=[2])
    Input.ForwardPropagation(feed=y_pred)
    Input.outbound.append(Loss)
    Loss.inbound.append(Input)
    loss_value = Loss.ForwardPropagation(y_true=y_true)
    # print(loss_value)
    # Todo check this test method
    assert loss_value[0] == 5 / y_true.shape[0] and loss_value[1] == 10 / y_true.shape[0]


def test_mae():
    fn = 'mae'
    y_pred = np.array([[3., 4.], [7., 6.]])
    y_true = np.array([[2, 1], [0, 0]])
    Loss = losses.get(fn)
    Input = InputLayer(shape=[2])
    Input.ForwardPropagation(feed=y_pred)
    Input.outbound.append(Loss)
    Loss.inbound.append(Input)
    loss_value = Loss.ForwardPropagation(y_true=y_true)
    # print(loss_value)
    # Todo check this test method
    assert loss_value[0] == 4 / y_true.shape[0] and loss_value[1] == 4.5 / y_true.shape[0]


def test_categorical_crossentropy():
    fn = 'categorical_crossentropy'
    y_pred = np.array([[0.28, 0.68, 0.04], [0.03, 0.95, 0.02]])
    y_true = np.array([[0, 1, 0], [0, 1, 0]])
    Loss = losses.get(fn)
    Input = InputLayer(shape=[3])
    Input.ForwardPropagation(feed=y_pred)
    Input.outbound.append(Loss)
    Loss.inbound.append(Input)
    loss_value = Loss.ForwardPropagation(y_true=y_true)
    # print(loss_value)
    assert 0.44 / y_true.shape[0] == round(loss_value, 2)


def test_binary_crossentropy():
    fn = 'binary_crossentropy'
    y_pred = np.array([0.28, 0.68])
    y_true = np.array([0, 1])
    Loss = losses.get(fn)
    Input = InputLayer(shape=[2])
    Input.ForwardPropagation(feed=y_pred)
    Input.outbound.append(Loss)
    Loss.inbound.append(Input)
    loss_value = Loss.ForwardPropagation(y_true=y_true)
    # print(loss_value)
    assert 0.357 == round(loss_value, 3)


def test_softmax_categorical_crossentropy():
    fn = 'softmax_categorical_crossentropy'
    y_pred = np.array([[0.9, 4.2, 0.3], [0.9, 4.2, 0.3]])
    y_true = np.array([[0., 1., 0.], [0., 1., 0.]])
    Loss = losses.get(fn)
    assert isinstance(Loss, losses.SoftmaxCategoricalCrossentropy)
    Input = InputLayer(shape=[3])
    Input.ForwardPropagation(feed=y_pred)
    Input.outbound.append(Loss)
    Loss.inbound.append(Input)
    loss_value = Loss.ForwardPropagation(y_true=y_true)
    Loss.BackwardPropagation()
    # print(loss_value)
    assert round(loss_value, 3) == round(0.027776516853274126, 3)
