"""
retina example that just feeds data from a retina to live output via an
intermediate population
"""
import spynnaker8 as p
from p8_integration_tests.base_test_case import BaseTestCase


def do_run():
    # Setup
    p.setup(timestep=1.0)

    # FPGA Retina - Down Polarity
    retina_device = p.external_devices.ExternalFPGARetinaDevice

    p.Population(
        2000, retina_device,
        {'spinnaker_link_id': 0, 'retina_key': 0x5,
         'mode': retina_device.MODE_128,
         'polarity': retina_device.DOWN_POLARITY},
        label='External spinnaker link')

    p.run(1000)
    p.end()


class SpinnakerLink1PopTest(BaseTestCase):

    def test_spinnaker_link_1pop(self):
        do_run()


if __name__ == "__main__":
    do_run()
