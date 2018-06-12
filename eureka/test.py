from eureka import client
import logging

logging.basicConfig()

ec = client.EurekaClient("MyApplication",
                         eureka_domain_name="localhost",
                         region="eu-west-1",
                         vip_address="http://localhost/",
                         port=8020,
                         secure_vip_address="https://localhost/",
                         secure_port=443
                         )
print(ec.get_zones_from_dns())
print(ec.get_eureka_urls())
print(ec.register())
print(ec.update_status("UP"))  # Or ec.register("UP")
print(ec.heartbeat())
