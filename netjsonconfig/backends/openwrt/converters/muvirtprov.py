from ..schema import schema
from .base import OpenWrtConverter

class MuVirtProvisioning(OpenWrtConverter):
	netjson_key = "muvirt-provisioning"
	intermediate_key = "muvirt-provisioning"
	_uci_types = ['virt']
	
	def __init__(self, *args, **kwargs):
		super(MuVirtProvisioning, self).__init__(*args,**kwargs)
    	
	def to_intermediate_loop(self, block, result, index=None):
		print("muvirt_prov intermediate loop:")
		result.setdefault('virt', [])
		block['.type'] = 'muvirt'
		block['.name'] = 'options'
		result['virt'] += [self.sorted_dict(block)]
		
		return result
		
	def to_netjson_loop(self, block, result, index):
		print("prov to_netjson_loop")
		return result