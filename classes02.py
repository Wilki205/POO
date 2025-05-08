from biblioteca import Conta

conta = Conta("001", "Wilkison Bruno", "Corrente", limite=500)
conta.ativarconta()
conta.depositar(1000)
conta.verificarsaldo()
conta.sacar(1200)
conta.verificarsaldo()
