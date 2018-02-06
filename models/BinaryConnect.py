import tensorflow as tf
import time
import numpy as np


def hard_sigmoid(x):
    return tf.clip_by_value((x + 1.) / 2, 0, 1)


def binarize(w, h, binary=True, deterministic=False):
    if not binary:
        wb = w
    else:
        if deterministic:
            wb = tf.where(tf.greater_equal(w, 0.), tf.ones_like(w), -tf.ones_like(w))
        else:
            sigma = hard_sigmoid(w / h)
            wb = tf.where(tf.greater_equal(sigma, tf.random_uniform(tf.shape(w), 0., 1., dtype=tf.float32)),
                          tf.ones_like(w), -tf.ones_like(w))
    return wb

