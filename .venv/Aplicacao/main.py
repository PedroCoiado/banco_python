# import Bibliotecario.crud_bibliotecario as bi

# bi.cadastrar("Helena Moraes","helana@gmail.com","11-5568-9966")
# bi.atualizar_bibliotecario(2,"Helena Moraes Dias", "helena.dias@uol.com.br","(11)9435-95954")
# bi.apagar_bibliotecario(2)
# bi.listar_bibliotecarios()

import Aluno.crud_aluno as al

# al.cadastrar("Ricardo Nogueira Matos","11234","Direito","corinthias2010@gmail.com","11 99393-3930")
# al.atualizar_aluno(1,"Ricardo Nogueira Matos Santos","11234","Direito","ricardo2003@gmail.com","11 99393-3930")
# al.apagar_aluno(1)
# al.listar_alunos()


# import publicacao.crud_publicacao as pu


# pu.cadastrar("Mitologia Nordica","Neil Gaiman","Intríseca","2017-02-24","8551001200","Ficção Histórica","Livro","Mitologia, Nordica, História, Vikings,Poderes",20,"Corredor 23")
# pu.atualizar_publicacao(1,"Mitologia Nordica","Neil Gaiman","Intríseca","2017-02-24","8551001200","Ficção Histórica","Livro","Mitologia, Nordica, História, Vikings,Poderes",20,"Corredor 23")
# pu.apagar_publicacao(1)
# pu.listar_publicacaos()

import Emprestimo.crud_emprestimo as em

# em.cadastrar("2024-02-28","",2,4,2)
em.atualizar_emprestimo("2024-07-12", 6)
em.listar_emprestimos()
