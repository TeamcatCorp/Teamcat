#coding=utf-8
'''
Created on 2016-7-6

@author: Administrator
'''

from teamvision.ci.viewmodels.plugins.vm_ci_plugin import VM_CIPlugin
from business.ci.ci_task_config_service import CITaskConfigService
from teamvision.ci.models import CITaskPlugin
from teamvision.ci.pagefactory.ci_template_path import CIPluginPath

class VM_SvnPlugin(VM_CIPlugin):
    '''
    classdocs
    '''
    plugin_id=1
    
    def __init__(self,plugin_parameter_dict):
        VM_CIPlugin.__init__(VM_SvnPlugin,plugin_parameter_dict)
        self.plugin=CITaskPlugin.objects.get(VM_SvnPlugin.plugin_id)
        self.repository_url=self.get_parameter_value('repository_url')
        self.local_directory=self.get_parameter_value('local_directory')
        self.ci_credentials=self.get_ci_credentials()
        self.svn_check_out_strategy=self.get_check_out_strategy()
        self.version="HEAD"
    
    
    def get_ci_credentials(self):
        result=0
        if self.get_parameter_value("ci_credentials"):
            result=int(self.get_parameter_value("ci_credentials"))
        return result
    
    def get_check_out_strategy(self):
        result=0
        if self.get_parameter_value("svn_check_out_strategy"):
            result=int(self.get_parameter_value("svn_check_out_strategy"))
        return result
    
    def get_template_path(self):
        return CIPluginPath.svn_plugin
    

        
        
        
    
    
   
    
    
    
                
        