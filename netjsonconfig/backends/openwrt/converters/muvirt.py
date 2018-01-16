from ..schema import schema
from .base import OpenWrtConverter
from collections import OrderedDict


class MuVirt(OpenWrtConverter):
	netjson_key = "muvirt"
	intermediate_key = "muvirt"
	_uci_types = ['virt','vm']
	_muvirt_schema = schema["properties"]["muvirt"]["items"]
	
	def __init__(self, *args, **kwargs):
		super(MuVirt, self).__init__(*args, **kwargs)
	
#	def _create_vmblock(self, result, vmname):
#		return result
#		
#	def to_intermediate(self):
#		result = OrderedDict()
#		
#		netjson = self.get_copy(self.netjson, self.netjson_key)
#		
#		if isinstance(netjson, list):
#			for obj in netjson:
#				vmname = obj['name']
#				result = self._create_vmblock(self,result,vmname)
#		return result

	def _create_disk(self,diskblock):
		block = self.sorted_dict(diskblock)
		block['.type'] = 'disk'
		block['.name'] = diskblock['identifier']
		block.pop('identifier')
		return block
    	
	def to_intermediate_loop(self, block, result, index=None):
		print("to_intermediate_loop")
		print(block)
		
	
		macs = []
		networks = []
		disknames = []
		
		package_name = 'virt'
		result.setdefault(package_name,[])
		block['.type'] = 'vm'
		block['.name'] = block['name']
		block.pop('name')
		
		if ("disk" in block):
			disks = block.pop('disk')
			for d in disks:
				diskblock = self._create_disk(d)
				result[package_name] += [self.sorted_dict(diskblock)] 
				disknames.append(d['identifier'])
				
		if ("network" in block):
			networkblock = block.pop('network')
			for net in networkblock:
				macs.append(net['mac'])
				networks.append(net['name'])
		
		block['mac'] = macs
		block['network'] = networks
		block['disks'] = disknames
		
		if ("provisioned" in block and block["provisioned"] == False):
			block.pop("provisioned")
			
		result[package_name] += [self.sorted_dict(block)] 
#		result['virt'] += {'foo':'bar'}
		return result
        
	def to_netjson_loop(self, block, result, index):
		print("to_netjson_loop")
		return result
#		print("to_netjson_loop")
#    	result.setdefault('virt', [])
#    	result['virt'] += {'foo':'bar'}
#    	return result