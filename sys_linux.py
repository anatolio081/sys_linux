import subprocess
import sys


class sys_linux:

    def get_net_interfaces(self):
        """
        Отобразить сетевые интерфейсы
        :return:
        """
        process = subprocess.run(['ip', 'link', 'show'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "list of interfaces:\n" + bytes.decode(output, "utf-8")
        return out

    def get_def_route(self):
        """
        Отобразить Маршрут по умолчанию
        :return:
        """
        p = subprocess.Popen('ip route | grep default', stdout=subprocess.PIPE,
                             shell=True)
        output, _ = p.communicate()
        out = "default route is : \n" + bytes.decode(output, "utf-8")
        return out

    def get_cpu_info(self):
        """
        Отобразить информацию о состоянии процессора
        :return:
        """
        process = subprocess.run(['lscpu'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "CpuInfo : \n" + bytes.decode(output, "utf-8")
        return out

    def get_proc_info_by_PID(self, PID):
        """
        Отобразить информацию о процессе
        :param PID:PID процесса
        :return:
        """
        process = subprocess.run(['ps', '-fp', str(PID)], stdout=subprocess.PIPE)
        output = process.stdout
        out = "Process info with PID= " + str(PID) + " : \n" + bytes.decode(output, "utf-8")
        return out

    def get_process_list(self):
        """
        Список всех процессов
        :return:
        """
        process = subprocess.run(['ps', '-e'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "List of all processes : \n" + bytes.decode(output, "utf-8")
        return out

    def get_net_info(self):
        """
        Отобразить статистику работы сетевых интерфейсов
        :return:
        """
        process = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "list of interfaces:\n" + bytes.decode(output, "utf-8")
        return out

    def get_service_status(self, service_name):
        """
        Отобразить статус работы сервиса
        :param service_name:имя сервиса
        :return:
        """
        process = subprocess.run(['service', str(service_name), 'status'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "status of " + str(service_name) + " : \n" + bytes.decode(output, "utf-8")
        return out

    def get_tcp_ports_status(self):
        """
        Отобразить состояние tcp портов сервера
        :return:
        """
        process = subprocess.run(['ss', '-p'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "Tcp Ports status:\n" + bytes.decode(output, "utf-8")
        return out

    def get_pack_ver(self, package_name):
        """
        Отобразить версию пакета
        :param package_name: имя пакета
        :return:
        """
        p = subprocess.Popen('apt-cache show ' + package_name + ' | grep Version||version', stdout=subprocess.PIPE,
                             shell=True)
        output, _ = p.communicate()
        out = package_name + " : \n" + bytes.decode(output, "utf-8")
        return out

    def get_list_files_in_dir(self, dir):
        """
        Отобразить список файлов в директории
        :param dir:путь к директории
        :return:
        """
        process = subprocess.run(['ls', dir], stdout=subprocess.PIPE)
        output = process.stdout
        out = "list of files in " + dir + ":\n" + bytes.decode(output, "utf-8")
        return out

    def get_cur_dir(self):
        """
        Отобразить текущую директорию
        :return:
        """
        process = subprocess.run(['pwd'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "current directory is:" + bytes.decode(output, "utf-8")
        return out

    def get_linux_core_v(self):
        """
        Отобразить версию ядра Linux
        :return:
        """
        process = subprocess.run(['uname', '-r'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "version of linux core:" + bytes.decode(output, "utf-8")
        return out

    def get_OS_v(self):
        """
        Отобразить версию операционной системы
        :return:
        """
        process = subprocess.run(['cat', '/etc/issue'], stdout=subprocess.PIPE)
        output = process.stdout
        out = "version of linux OS:" + bytes.decode(output, "utf-8")
        return out

    def show_params(self):
        """
        Отобразить список параметров
        :return:
        """
        print("try to use one of parameters:\n"
              "\tget_net_interfaces\n"
              "\tget_def_route\n"
              "\tget_cpu_info\n"
              "\tget_proc_info_by_PID xx -where xx is PID\n"
              "\tget_process_list\n"
              "\tget_net_info\n"
              "\tget_service_status xx -where xx is a service name\n"
              "\tget_tcp_ports_status\n"
              "\tget_pack_ver xx -where xx is a package name\n"
              "\tget_list_files_in_dir xx -where xx is a directory\n"
              "\tget_cur_dir\n"
              "\tget_linux_core_v\n"
              "\tget_OS_v\n")


linux_helper = sys_linux()
try:
    if sys.argv[1] == "get_net_interfaces":
        print(linux_helper.get_net_interfaces())
    elif sys.argv[1] == "get_def_route":
        print(linux_helper.get_def_route())
    elif sys.argv[1] == "get_cpu_info":
        print(linux_helper.get_cpu_info())
    elif sys.argv[1] == "get_proc_info_by_PID":
        try:
            print(linux_helper.get_proc_info_by_PID(sys.argv[2]))
        except IndexError:
            print("Parameter PID is not found")
    elif sys.argv[1] == "get_process_list":
        print(linux_helper.get_process_list())
    elif sys.argv[1] == "get_net_info":
        print(linux_helper.get_net_info())
    elif sys.argv[1] == "get_service_status":
        try:
            print(linux_helper.get_service_status(sys.argv[2]))
        except IndexError:
            print("Parameter service name is not found")
    elif sys.argv[1] == "get_tcp_ports_status":
        print(linux_helper.get_tcp_ports_status())
    elif sys.argv[1] == "get_pack_ver":
        try:
            print(linux_helper.get_pack_ver(sys.argv[2]))
        except IndexError:
            print("Parameter package name is not found")
    elif sys.argv[1] == "get_list_files_in_dir":
        try:
            print(linux_helper.get_list_files_in_dir(sys.argv[2]))
        except IndexError:
            print("Parameter directory is not found")
    elif sys.argv[1] == "get_cur_dir":
        print(linux_helper.get_cur_dir())
    elif sys.argv[1] == "get_linux_core_v":
        print(linux_helper.get_linux_core_v())
    elif sys.argv[1] == "get_OS_v":
        print(linux_helper.get_OS_v())
    else:
        print("first param is not valid")
        linux_helper.show_params()
except IndexError:
    print("first param is not found")
    linux_helper.show_params()
