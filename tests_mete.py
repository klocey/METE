"""Tests for the METE (Maximum Entropy Theory of Ecology) Module"""

from mete import *
import nose
from nose.tools import assert_almost_equals, assert_equals
from decimal import Decimal

#Fitted values of parameters from Harte 2011. The fits were done using different
#software and therefore represent reasonable tests of the implemented algorithms
#Numbers with decimal places are entered as strings to allow Decimal to properly handle them
table7pt2 = [[4, 16, 64, '0.0459', '0.116', '5.4', '-0.037', '0.083', '0.74'],
             [4, 64, 256, '-0.00884', '0.0148', '5.3', '-0.030', '0.021', '-0.56'],
             [4, 1024, 4096, '-0.00161', '0.000516', '5.3', '-0.0029', '0.0013', '-1.6'],
             [4, 16384, 65536, '-0.000135', '0.0000229', '5.3', '-0.00022', '0.0000881', '-2.3'],
             [4, 16, 16384, '0.0459', '0.116', '4.0', '0.046', '0.00024', '0.74'],
             [4, 64, 65536, '-0.00884', '0.0148', '4.0', '-0.0089', '0.000061', '-0.6'],
             [4, 1024, 1048576, '-0.00161', '0.000516', '4.0', '-0.0016', '0.00000382', '-1.6'],
             [4, 16384, 16777216, '-0.000135', '0.0000229', '4.0', '-0.00014', '0.000000239', '-2.3'],
             [16, 64, 256, '0.101', '0.116', '21.4', '0.018', '0.083', '6.4'],
             [16, 256, 1024, '0.0142', '0.0148', '21.3', '-0.0066', '0.021', '3.6'],
             [16, 4096, 16384, '0.000413', '0.000516', '21.3', '-0.00089', '0.0013', '1.7'],
             [16, 65536, 262144, '0.0000122', '0.0000229', '21.3', '-0.000069', '0.000081', '0.79'],
             [16, 64, 65536, '0.101', '0.116', '16.1', '0.10', '0.0024', '6.4'],
             [16, 256, 262144, '0.0142', '0.0148', '16.0', '0.014', '0.000061', '3.6'],
             [16, 4096, 4194304, '0.000413', '0.000516', '16.0', '0.00041', '0.00000382', '1.7'],
             [16, 65536, 67108864, '0.0000122', '0.0000229', '16.0', '0.000012', '0.000000239', '0.79'],
             [64, 256, 1024, '0.102'],
             [64, 1024, 4096, '0.0147'],
             [64, 16384, 65536, '0.000516'],
             [64, 262144, 1048576, '0.0000228'],
             [64, 256, 262144, '0.102'],
             [64, 1024, 1048576, '0.0147'],
             [64, 16384, 16777216, '0.000516'],
             [64, 262144, 268435456, '0.0000228'],
             [256, 1024, 4096, '0.102'],
             [256, 4096, 16384, '0.0147'],
             [256, 65536, 262144, '0.000516'],
             [256, 1048576, 4194304, '0.0000228'],
             [256, 1024, 1048576, '0.102'],
             [256, 4096, 4194304, '0.0147'],
             [256, 65536, 67108864, '0.000516'],
             [256, 1048576, 1073741824, '0.0000228']]

def test_get_lambda_sad():
    """Tests SAD lambda estimates against values from Table 7.2 of Harte 2011
    
    The table of test values is structured as S0, N0, Beta
    
    """
    data = set([(line[0], line[1], line[3]) for line in table7pt2])
    for line in data:
        yield check_get_lambda_sad, line[0], line[1], line[2]
        
def check_get_lambda_sad(S0, N0, beta_known):
    beta_code = get_lambda_sad(S0, N0)
    
    #Determine number of decimal places in known value and round code value equilalently
    decimal_places_in_beta_known = abs(Decimal(beta_known).as_tuple().exponent)
    beta_code_rounded = round(beta_code, decimal_places_in_beta_known)
    
    assert_almost_equals(beta_code_rounded, float(beta_known), places=6)
    
if __name__ == "__main__":
    nose.run()