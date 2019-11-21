# sys_linux
Домашка по subprocess
Пример использования:
    python sys_linux.py param1 param2
Где первый парметр-метода обязателен, вот список параметров:
    get_net_interfaces
    get_def_route
    get_cpu_info
    get_proc_info_by_PID
    get_process_list
    get_net_info
    get_service_status
    get_tcp_ports_status
    get_pack_ver
    get_list_files_in_dir
    get_cur_dir
    get_linux_core_v
    get_OS_v

Для некоторого списка методов требуется ввести доп параметр
     get_proc_info_by_PID xx - вместо хх требуется подставить PID процесса
     get_service_status xx - вместо хх требуется подставить имя сервиса
     get_pack_ver xx - вместо хх требуется подставить имя пакета
     get_list_files_in_dir xx - вместо хх требуется подставить путь к директории