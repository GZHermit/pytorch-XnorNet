# coding:utf-8
import datetime
import os

import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('max_steps', 225000, 'Max number of steps.')
tf.app.flags.DEFINE_integer('batch_size', 100, 'Batch size.  Must divide evenly into the dataset sizes.')
tf.app.flags.DEFINE_integer('learning_rate', 0.01, 'Initial learning rate.')
tf.app.flags.DEFINE_string('log_dir', './log', 'Directory to put the log data.')
tf.app.flags.DEFINE_string('run_name', '', 'Name for the run (for logging).')
tf.app.flags.DEFINE_boolean('binary', True, 'Toggle binary-connect usage.')
tf.app.flags.DEFINE_boolean('deteministic', True, 'Switch between stochastic and deteministic binary-connect.')


def main(_):
    FLAGS.run_name = \
        datetime.datetime.now().strftime("%y%m%d_%H%M%S") + \
        FLAGS.run_name + \
        'BIN_' + str(FLAGS.binary) + \
        'Deter_' + str(FLAGS.deteministic)

    FLAGS.log_dir = os.path.join(FLAGS.log_dir, FLAGS.run_name)
    if tf.gfile.Exists(FLAGS.log_dir):
        tf.gfile.DeleteRecursively(FLAGS.log_dir)
    tf.gfile.MakeDirs(FLAGS.log_dir)
    print(FLAGS.run_name)

if __name__ == '__main__':
    tf.app.run()
