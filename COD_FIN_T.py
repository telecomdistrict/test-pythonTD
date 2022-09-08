from getpass import getpass
from pydoc import doc
from netmiko import ConnectHandler
import datetime
import time
#contra= open('./prueba.txt', 'rt', encoding='utf-8')
#cont= contra.readline()
 
devices = [{
    "device_type": "cisco_xr",
    "ip": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "22",
}]
n = 0
#while True:
for device in devices:
    net_connect = ConnectHandler(**device)
    
    output_1 = net_connect.send_command("sh bgp vrf TEF_LTE summ | inc \"64802|7438|Neighbor\"")
    output_2 = net_connect.send_command("sh bgp vrf TEF_3G_IuR summ | inc \"64802|7438|Neighbor\"")
    output_3 = net_connect.send_command("sh bgp vrf TEF_3G_IuB summ | inc \"64802|7438|Neighbor\"")
    output_4 = net_connect.send_command("sh bgp vrf TEF_3G_Voice summ | inc \"64802|7438|Neighbor\"")
    output_5 = net_connect.send_command("sh bgp vrf TEF_3G_Control summ | inc \"64802|7438|Neighbor\"")
    output_6 = net_connect.send_command("sh bgp vrf TEF_3G_OAM summ | inc \"64802|7438|Neighbor\"")
    output_7 = net_connect.send_command("sh bgp vrf TEF_3G_Data summ | inc \"64802|7438|Neighbor\"")
    output_8 = net_connect.send_command("show bgp sessions")
    output_9 = net_connect.send_command("show bfd session")
    output_10 = net_connect.send_command("show bundle brief")

    net_connect.disconnect()


documento= datetime.datetime.now()

def create_file(): 
    
    
    with open(documento.strftime("%d %B %Y- Hora_%H-%M-%S" )+".txt", "w") as documentacion: 
        documentacion.write(f"\n{'#' * 50}\nBGP sessions stablishes per VRF \n{'#' * 50}\n") 
        documentacion.write("*"*100)
        documentacion.write("\n")
        documentacion.write("==============>IP host = "+net_connect.host)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("=============sh bgp vrf TEF_LTE summ | inc \"64802|7438|Neighbor================")
        documentacion.write("\n")
        documentacion.write(output_1)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("=============sh bgp vrf TEF_3G_IuR summ | inc \"64802|7438|Neighbor\"===========")
        documentacion.write("\n")
        documentacion.write(output_2)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("=============sh bgp vrf TEF_3G_IuB summ | inc \"64802|7438|Neighbor\"===========")
        documentacion.write("\n")
        documentacion.write(output_3)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("============sh bgp vrf TEF_3G_Voice summ | inc \"64802|7438|Neighbor\"==========")
        documentacion.write("\n")
        documentacion.write(output_4)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("=============sh bgp vrf TEF_3G_Control summ | inc \"64802|7438|Neighbor\"=======")
        documentacion.write("\n")
        documentacion.write(output_5)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("=============sh bgp vrf TEF_3G_OAM summ | inc \"64802|7438|Neighbor\"===========")
        documentacion.write("\n")
        documentacion.write(output_6)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("=============sh bgp vrf TEF_3G_Data summ | inc \"64802|7438|Neighbor\"==========")
        documentacion.write("\n")
        documentacion.write(output_7)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("==============show bgp sessions=================================================")
        documentacion.write("\n")
        documentacion.write(output_8)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("===============show bfd session=================================================")
        documentacion.write("\n")
        documentacion.write(output_9)
        documentacion.write("\n")
        documentacion.write("-"*100)
        documentacion.write("\n")
        documentacion.write("================show bundle brief===============================================")
        documentacion.write("\n")
        documentacion.write(output_10)
  
create_file() 
