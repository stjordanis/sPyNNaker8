import numpy

from p8_integration_tests.base_test_case import BaseTestCase
from p8_integration_tests.scripts.synfire_run import SynfireRunner

n_neurons = 20  # number of neurons in each population
runtimes = [0, 100]  # The zero uis to read data before a run
neurons_per_core = None
weight_to_spike = 1.0
delay = 1
placement_constraint = (0, 0, 9)
get_weights = True
get_delays = True


class SynfireProjectionOnSameChip(BaseTestCase):

    def test_get_before_and_after(self):
        synfire_run = SynfireRunner()
        synfire_run.do_run(n_neurons, neurons_per_core=neurons_per_core,
                           weight_to_spike=weight_to_spike, delay=delay,
                           placement_constraint=placement_constraint,
                           run_times=runtimes, get_weights=get_weights,
                           get_delays=get_delays)
        weights = synfire_run.get_weights()
        self.assertEquals(n_neurons, len(weights[0]))
        self.assertEquals(n_neurons, len(weights[1]))
        self.assertTrue(numpy.allclose(weights[0][0][2], weights[1][0][2]))

        delays = synfire_run.get_delay()
        self.assertEquals(n_neurons, len(delays[0]))
        self.assertEquals(n_neurons, len(delays[1]))
        self.assertTrue(numpy.allclose(delays[0][0][2], delays[1][0][2]))


if __name__ == '__main__':
    synfire_run = SynfireRunner()
    synfire_run.do_run(n_neurons, neurons_per_core=neurons_per_core,
                       weight_to_spike=weight_to_spike, delay=delay,
                       placement_constraint=placement_constraint,
                       run_times=runtimes, get_weights=get_weights,
                       get_delays=get_delays)
    weights = synfire_run.get_weights()
    delays = synfire_run.get_delay()
    print("weights[0]")
    print(weights[0])
    print(weights[0].shape)
    print("weights[1]")
    print(weights[1])
    print(weights[1].shape)
    print("delays[0]")
    print(delays[0])
    print(delays[0].shape)
    print("delays[1]")
    print(delays[1])
    print(delays[1].shape)
