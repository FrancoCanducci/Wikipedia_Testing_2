# Wikipedia_Testing_2

Este script em Python utiliza Selenium para automatizar a busca e a navegação em uma página da Wikipedia sobre o software Selenium. Ele demonstra como realizar interações básicas com uma página web e medir o tempo de execução de operações específicas.


Funcionalidades

Modo Headless: O script pode ser executado tanto com a interface gráfica visível quanto em modo headless (sem interface gráfica), configurável através do uso de options.add_argument('--headless').

Busca e Navegação: O script busca pelo campo de busca na página da Wikipedia sobre Selenium, digita o termo "História" e pressiona Enter para realizar a busca.

Medição de Tempo: O script mede o tempo total necessário para buscar e carregar a página após a entrada do termo "História".

Captura de Tela em Caso de Timeout: Em caso de timeout ao tentar encontrar o campo de busca, o script captura uma tela (screenshot.png) para fins de depuração.

Observações
Certifique-se de substituir a localização do WebDriver do Chrome no código caso ele não esteja localizado no mesmo diretório ou no PATH do sistema.

A URL utilizada neste exemplo é 'https://pt.wikipedia.org/wiki/Selenium_(software)'. Certifique-se de ajustar a URL conforme necessário para outras páginas da Wikipedia ou sites.
