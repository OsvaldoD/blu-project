from django.db import models

# Create your models here.

class Message(models.Model):
    SALDO = 'SALDO'
    EXTRATO = 'EXTRATO'
    ABERTURA_CONTA = 'ABERTURA_CONTA'
    CONF_PAGAMENTO = 'CONFIRMACAO DE PAGAMENTO'
    PEDIDO_FX = 'PEDIDO DE FX'
    OUTRO = 'OUTRO'

    CATEGORIA_MENSAGEM_CHOICES = (
        (SALDO, 'Pedir saldo'),
        (EXTRATO, 'Pedir extrato'),
        (ABERTURA_CONTA, 'Abertura de conta'),
        (CONF_PAGAMENTO, 'Confirmacao de pagamento'),
        (PEDIDO_FX, 'Pedido de FX'),
        (OUTRO, 'Outro'),
    )

    categoria = models.CharField(max_length=50, choices=CATEGORIA_MENSAGEM_CHOICES, default=SALDO)
    nome = models.CharField(max_length=5)
    email = models.EmailField()
    message = models.TextField( verbose_name='Mensagem')

    def __str__(self):
        return '{}'.format(self.categoria)



class Credito(models.Model):
    nome = models.CharField(max_length=50, verbose_name= 'Nome')
    apelido = models.CharField(max_length=50, verbose_name='Apelido do cliente')
    contacto= models.CharField(max_length=30)
    email = models.EmailField(blank=False)
    nome_empresa = models.CharField(max_length=60)
    numero_conta = models.CharField(max_length=30)
    data_proposta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.nome, self.apelido)







