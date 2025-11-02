Descrição
Aplicação de linha de comando para criptografia e descriptografia de mensagens utilizando a implementação Fernet da biblioteca cryptography. O objetivo é fornecer uma solução simples e segura para trocar mensagens: o remetente gera uma chave e cifra a mensagem; o destinatário utiliza a mesma chave para decifrar o ciphertext.

Arquivos

encrypt.py — gera (ou aceita) uma chave, recebe a mensagem do usuário e imprime o ciphertext (não grava em disco por padrão).

decrypt.py — recebe a chave e o ciphertext (copiados/colados pelo usuário) e imprime a mensagem descriptografada.

Fluxo de uso

Remetente executa encrypt.py, gera/obtém uma chave e cifra a mensagem, obtendo um ciphertext.

Remetente envia o ciphertext ao destinatário por canal A (ex.: e-mail, drive).

Remetente transmite a chave ao destinatário por um canal separado e seguro (ex.: SMS, ligação).

Destinatário executa decrypt.py, cola a chave e o ciphertext e recupera a mensagem original.

Dependências

cryptography — para Fernet (confidencialidade e integridade).

getpass — para entrada segura de chaves/senhas no terminal.

Boas práticas de segurança

Nunca envie a chave e o ciphertext pelo mesmo canal.

Use chaves/ senhas fortes; códigos curtos são vulneráveis a ataques de força bruta.

Guarde a chave em local seguro e nunca a publique em repositórios públicos.

Para casos de maior sensibilidade, considere um fluxo com criptografia híbrida (chave simétrica cifrada por chave pública) e proteção adicional do canal.
