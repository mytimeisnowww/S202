from ProductAnalyzer import ProductAnalyzer
from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

p1 = ProductAnalyzer(db)
p1.produtoMaisVendido()
writeAJson(p1.totalDeVendas(), "Total de Vendas")
p2 = ProductAnalyzer(db)
p2.produtoMaisVendido()
writeAJson(p2.produtoMaisVendido(), "Produto mais vendido")
p3 = ProductAnalyzer(db)
p3.clienteQueMaisGastou()
writeAJson(p3.clienteQueMaisGastou(), "Cliente Que mais gastou em uma única compra")
p4 = ProductAnalyzer(db)
p4.produtosQueTiveramUmaQuantidadeVendidaAcimaDe1Unidades()
writeAJson(p4.produtosQueTiveramUmaQuantidadeVendidaAcimaDe1Unidades(), "Produtos que tiveram uma quantidade vendida acima de 1 unidades")
