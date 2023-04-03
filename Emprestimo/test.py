import  unittest
import coverage

cov= coverage.Coverage()
cov.start()


def ValidaEmprestimo(aplicante,renda,moradores,tipo):

    emprestimo=True


    if aplicante!="Pessoas":
        emprestimo=False
    
    if renda <1000.00 or renda > 83000.00:
        emprestimo=False
    
    if moradores >5:
        emprestimo=False
    
    if tipo != "Condominio" or "Sobrado" or "Casa Térrea":
        emprestimo=False
    
    if emprestimo== True:
        return True
    else:
        return False
    

class TestStringMethods(unittest.TestCase):

    def testValidaEmprestimo(self):
        emprestimo= ValidaEmprestimo("Pessoas",1000.00,5,"Sobrado")
        self.assertEquals(emprestimo,False)

    def testValidaEmprestimo1(self):
        emprestimo= ValidaEmprestimo("Pessoas",1500.00,4,"Casa")
        self.assertEquals(emprestimo,False)    


    def testValidaEmprestimo1(self):
        emprestimo= ValidaEmprestimo("Pessoas",85000.00,3,"Condominio")
        self.assertEquals(emprestimo,False)  

    def testValidaEmprestimo2(self):
            emprestimo= ValidaEmprestimo("Pessoas",99,1,"Condominio")
            self.assertEquals(emprestimo,False)    

    def testValidaEmprestimo3(self):
            emprestimo= ValidaEmprestimo("Pessoas",1000000.00000,9,"Ca")
            self.assertEquals(emprestimo,False) 


if __name__ == '__main__':
    cov.stop()
    cov.save()
    cov.report()
    unittest.main()


''