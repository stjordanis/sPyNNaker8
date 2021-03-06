import spynnaker8 as p
from p8_integration_tests.base_test_case import BaseTestCase
import unittest


class TestMultiBoardSpikeOutput(BaseTestCase):

    counts = None

    @staticmethod
    def spike_receiver(label, time, neuron_ids):
        TestMultiBoardSpikeOutput.counts[label] += len(neuron_ids)

    def test_multi_board_spike_output(self):
        self.assert_not_spin_three()
        TestMultiBoardSpikeOutput.counts = dict()
        p.setup(1.0, n_chips_required=((48 * 2) + 1))
        machine = p.get_machine()

        labels = list()
        for chip in machine.ethernet_connected_chips:
            print("Adding population on {}, {}".format(chip.x, chip.y))
            label = "{}, {}".format(chip.x, chip.y)
            labels.append(label)
            spike_cells = {"spike_times": [i for i in range(100)]}
            pop = p.Population(10, p.SpikeSourceArray(**spike_cells),
                               label=label)
            pop.add_placement_constraint(chip.x, chip.y)
            p.external_devices.activate_live_output_for(pop)
            TestMultiBoardSpikeOutput.counts[label] = 0

        live_output = p.external_devices.SpynnakerLiveSpikesConnection(
            receive_labels=labels)
        for label in labels:
            live_output.add_receive_callback(
                label, TestMultiBoardSpikeOutput.spike_receiver)

        p.run(1000)
        p.end()

        for label in labels:
            print("Received {} of 1000 spikes from {}".format(
                TestMultiBoardSpikeOutput.counts[label], label))
            self.assertEqual(TestMultiBoardSpikeOutput.counts[label], 1000)


if __name__ == '__main__':
    unittest.main()
