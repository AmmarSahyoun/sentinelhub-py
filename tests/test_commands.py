import unittest
import subprocess
import os
from tests_all import TestSentinelHub


class TestCommands(TestSentinelHub):
    @classmethod
    def setUpClass(cls):
        cls.status = 0

        if not os.path.exists(cls.OUTPUT_FOLDER):
            os.mkdir(cls.OUTPUT_FOLDER)

        compact_product_id = 'S2A_MSIL1C_20170414T003551_N0204_R016_T54HVH_20170414T003551'
        cls.status += subprocess.call('sentinelhub.aws --product {} -rf ./{} -b B8A'.format(compact_product_id,
                                                                                            cls.OUTPUT_FOLDER),
                                      shell=True)
        old_product_id = 'S2A_OPER_PRD_MSIL1C_PDMC_20160121T043931_R069_V20160103T171947_20160103T171947'
        cls.status += subprocess.call('sentinelhub.aws --product {} -i'.format(old_product_id), shell=True)
        cls.status += subprocess.call('sentinelhub.aws --tile T38TML 2015-12-19 -ref {} '
                                      '--bands B01,B10'.format(cls.OUTPUT_FOLDER), shell=True)
        url = 'http://sentinel-s2-l1c.s3.amazonaws.com/tiles/54/H/VH/2017/4/14/0/metadata.xml'
        cls.status += subprocess.call('sentinelhub.download {} {}/example.xml -r'.format(url, cls.OUTPUT_FOLDER),
                                      shell=True)

        cls.status += subprocess.call('sentinelhub.config --show', shell=True)

        cls.status += subprocess.call('sentinelhub --help', shell=True)
        cls.status += subprocess.call('sentinelhub.aws --help', shell=True)
        cls.status += subprocess.call('sentinelhub.config --help', shell=True)
        cls.status += subprocess.call('sentinelhub.download --help', shell=True)

    def test_return_type(self):
        self.assertTrue(self.status == 0, "Commands failed")

# sentinelhub.aws --product S2A_MSIL2A_20180402T151801_N0207_R068_T33XWJ_20180402T202222
# sentinelhub.aws --tile T33XWJ 2018-04-02 --l2a


if __name__ == '__main__':
    unittest.main()
