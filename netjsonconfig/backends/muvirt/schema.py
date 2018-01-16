"""
muvirt specific JSON-schema definition
"""

from copy import deepcopy
from ...schema import schema as default_schema

base_muvirt_schema = {
	"$schema":"http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": True,
    "definitions": {
    	"virtual_disk": {
    		"title": "Virtual Disk",
    		"type": "object",
    		"properties": {
    			"identifier": {
    				"title": "Identifier",
    				"type": "string",
    				"description": "logical identifier for the disk in UCI, "
    								"will be automatically generated if left blank",
    				"maxLength": 15,
    				"propertyOrder": 7
    			},
    			"size": {
    				"title": "Volume Size (GB)",
    				"type":"integer"
    			},
    			"path": {
    				"title": "Volume Path",
    				"type": "string",
    				"description": "Volume path - if not specified, a LVM volume will be created"
    			},
    			"type": {
    				"title": "VM Device Type",
    				"type": "string",
    				"default": "virtio-blk"
    			}
    		}
    	},
    	"virtual_nic": {
    		"title": "Network Interface",
    		"type": "object",
    		"properties": {
    			"name": {
    				"title": "Network Name",
    				"type": "string",
    				"propertyOrder": 1
    			},
    			"mac": {
    				"title": "MAC address",
    				"type": "string",
    				"pattern": "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$",
    				"minLength": 17,
    				"maxLength": 17
    			}
    		}
    	},
    	"virtual_machine": {
    		"title": "Virtual Machine",
    		"type": "object",
    		"properties": {
    			"name": {
    				"title": "name",
    				"type": "string",
    				"propertyOrder": 1
    			},
    			"memory": {
    				"title": "Amount of RAM (MB)",
    				"type": "integer",
    				"propertyOrder": 2,
    				"default": 256
    			},
    			"numprocs": {
    				"title": "Number of vCPUs",
    				"type": "integer",
    				"propertyOrder": 3,
    				"default": 1,
    			},
    			"network": {
    				"type": "array",
    				"title": "Network Interfaces",
    				"items": {
    					"$ref": "#/definitions/virtual_nic"
    				},
    				"propertyOrder": 4
    			},
    			"disk": {
    				"type": "array",
    				"title": "Disks",
    				"propertyOrder": 5,
    				"items": {
    					"$ref": "#/definitions/virtual_disk"
    				}
    			},
    			"imageurl": {
    				"type": "string",
    				"title": "Image URL",
    				"description": "URL to download initial image from",
    				"propertyOrder": 6
    			},
    			"provisioned": {
    				"type": "boolean",
    				"title": "VM Provisioned?",
    				"description": "This flag is set when the VM has been provisioned "
    					"(i.e the image has been downloaded and copied)",
    				"default": False,
					"propertyOrder": 7
				},
				"cloudinit": {
    				"type": "string",
    				"title": "Cloud init script (optional)",
    				"description": "Path to the cloud init file. Either a local path or http/https "
    					"(Tip: Use the Files section to distribute files to the device)."
    					"The downloaded file will be wrapped into a vfat image called cidata.",
    				"default": "",
    				"propertyOrder": 8
    			},
    			"telnet": {
    				"type": "integer",
    				"title": "Telnet console port",
    				"description": "Port to spawn ttyS0 serial console on",
    				"default": 4446,
    				"propertyOrder": 9
    			},
    			"enable": {
    				"title": "Enable this VM?",
    				"type": "boolean",
    				"default": True,
    				"propertyOrder": 10
    			},
    		}
    	}
    },
    "properties": {
    	"muvirt": {
    		"type": "array",
    		"title": "Virtual Machines",
            "propertyOrder": 20,
            "items": {
            			"$ref": "#/definitions/virtual_machine"
            	}
        },
        "muvirt-provisioning": {
        	"title": "Virtalization Provisioning",
    		"type": "object",
    		"propertyOrder": 21,
    		"properties": {
    			"scratch": {
    				"title": "Scratch folder path",
    				"type": "string",
    				"description": "Directory to temporarily hold VM images",
    				"propertyOrder": 1
    			},
    			"hugetlb": {
    				"title": "Memory to reserve for virtual machines",
    				"type": "integer",
    				"description": "Amount of RAM to reserve for huge pages/hugetlbfs - used for "
    					"virtual machines and DPDK",
    				"propertyOrder": 2
    			}
    		}
        }
    }
}