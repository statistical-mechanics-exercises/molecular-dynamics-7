import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_kinetic(self) : 
        for i in range(10) :
            vel = np.zeros([7,2])
            myeng = 0
            for j in range(7) : 
               vel[j,0], vel[j,1] = np.random.normal(), np.random.normal()
               myeng = myeng + vel[j,0]*vel[j,0] / 2 + vel[j,1]*vel[j,1] / 2
            self.assertTrue( np.abs( kinetic(vel) - myeng )<1E-6, "The kinetic energy is computed incorrectly" )
            
    def test_kinetic_energy(self) : 
        # IMPROVE THIS TEST -- ASK MICHELINO
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        times, this_ke = zip(*figdat)
        # Calculate the average kinetic energy
        average_ke = sum(this_ke) / len(this_ke)
        self.assertTrue( np.abs( np.abs( average_ke - 7*temperature ) )<0.5, "The average kinetic energy is not correct" )
       
    def test_forces(self) : 
        pp = pos
        # Get the positions and analytic forces
        base_p, base_f = potential(pp)
        for i in range(7) :
            for j in range(2) :
                pp[i][j] = pp[i][j] + 1E-8
                new_p, crap = potential(pp)
                numder = (new_p-base_p)/1E-8
                self.assertTrue( np.abs(numder + base_f[i][j])<1e-4, "Forces and potential are not consistent" )
                pp[i][j] = pp[i][j] - 1E-8
