import os 
import sys 
from llm import read_code
from prompts import *


allowed_extensions = ['.py']
ignored_extensions = ['__pycache__']

# 具体文件分析 
def analyse_file(file_path, save_path):
    
    print(f'\n-- analyse_file : {file_path} ' ) 
    if os.path.isfile(save_path):return '' 
    
    file_extension = os.path.splitext(file_path)[-1]
    if not file_extension in allowed_extensions : return ''
    
    code = open(file_path).read().strip() 
    if len(code) == 0:return ''
    
    system_prompt_code1 = system_prompt_code.substitute(file_extension=file_extension) 
    user_prompt_code1 = user_prompt_code.substitute(code=code, file_extension=file_extension) 
    # content = 'test'
    content = read_code(system_prompt=system_prompt_code1, user_prompt=user_prompt_code1) 
    print(f'-- read_file : {content} ' ) 
    if content.startswith('```'):content=content[3:]
    if content.endswith('```'):content=content[:-3]
    
    with open(save_path, 'w') as f:f.write(content) 
    
    return content


# 对已有的分析 生成总的分析 
def analyse_module(analyse_files, save_path, root_dir):
    
    analyse_files.sort()
    whole_content = ''
    
    if os.path.isfile(save_path):return ''
    
    for file_path in analyse_files:
        if file_path.find('.DS_Store') != -1:continue
        if not os.path.isfile(file_path):continue 
        
        content = open(file_path).read().strip()
        if len(content) == 0:continue
        
        whole_content += '\n***\n文件：' + file_path.replace(root_dir, '') + '\n文件内容分析：\n'  + content       
    
    user_prompt_module1 = user_prompt_module.substitute(whole_content=whole_content)  
    content = read_code(system_prompt=system_prompt_module, user_prompt=user_prompt_module1)  
    if content.startswith('```'):content=content[3:]
    if content.endswith('```'):content=content[:-3] 
    print(f'\n-- analyse_module : {content} ' ) 
    
    with open(save_path, 'w') as f:f.write(content) 
    
    return content


# 对文件夹内的模块内容进行整体分析 
def analyse_sub_dir(dir_path, root_dir, reader_dir):
    
    sub_path_names = os.listdir(dir_path)
    sub_path_names.sort()
    print(f'\n-- analyse_sub_dir : {dir_path} | {len(sub_path_names)}' )  
    
    module_analyse_files = []
        
    for sub_path_name in sub_path_names:
        if sub_path_name in ignored_extensions:continue
        
        sub_path = os.path.join(dir_path, sub_path_name)
        
        if os.path.isfile(sub_path):
            save_name = sub_path.replace(root_dir, '').replace('/','--')  
            save_path = os.path.join(reader_dir, save_name + '.md') 
            analyse_file(sub_path, save_path)  
            
            module_analyse_files.append(save_path) 
              
        if os.path.isdir(sub_path):  
            module_analyse_save_path =  analyse_sub_dir(sub_path, root_dir, reader_dir)
           
            module_analyse_files.append(module_analyse_save_path)    
           
        
    # 模块整体分析 
    module_name = dir_path.replace(root_dir, '').replace('/', '--').strip()
    if len(module_name) == 0:module_name = 'index' 
    
    module_analyse_save_path = os.path.join(reader_dir, f'module_{module_name}.md' )  
    analyse_module(module_analyse_files, module_analyse_save_path, root_dir)
    
    return module_analyse_save_path
             
     

if __name__ == '__main__':
    
    path = sys.argv[1] 
    
    if os.path.isfile(path):
        save_path = path + '.md'  
        analyse_file(path, save_path)
        
    elif os.path.isdir(path): 
        reader_dir = path + '_analyse'
        if not os.path.isdir(reader_dir):os.makedirs(reader_dir)  
        if not path.endswith('/'):path = path + '/' 
        analyse_sub_dir(path, path, reader_dir)
        