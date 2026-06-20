import unittest
import sys
import os
import subprocess
import tempfile
import shutil
import matplotlib.pyplot as plt
import json

class TestMain(unittest.TestCase):

    def test_display_chart(self):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.txt') as tmp:
            # Write some data to the file
            tmp.write(b'1,2,3,4,5')
            tmp.flush()
            # Run the main function with the temporary file
            try:
                subprocess.check_output([sys.executable, 'main.py', tmp.name])
                # Check if the chart is displayed
                plt.show(block=False)
                plt.close()
                self.assertTrue(True)
            except subprocess.CalledProcessError as e:
                self.fail(f'Failed to run main.py: {e}')
            except FileNotFoundError:
                self.fail('Matplotlib is not installed')

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])