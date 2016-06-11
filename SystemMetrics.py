import psutil


class SystemMetrics:
    def __init__(self):
        self._cpu_metrics = dict()
        self._disk_metrics = dict()
        self._memory_metrics = dict()
        self._system_metric = dict()
        self._network_metric = dict()

    @staticmethod
    def cpu_times():
        cpu_times_metrics = {}
        cp_metrics = psutil.cpu_times(percpu=False)
        cpu_times_metrics['user'] = cp_metrics.user
        cpu_times_metrics['system'] = cp_metrics.system
        cpu_times_metrics['idle'] = cp_metrics.idle
        cpu_times_metrics['nice'] = cp_metrics.nice

        return cpu_times_metrics

    @staticmethod
    def cpu_usage():
        cpu_usage_metrics = dict()
        cpu_usage_metrics['cpu_count'] = psutil.cpu_count(logical=True)
        cpu_usage_metrics['cpu_percent'] = psutil.cpu_percent(interval=1)
        cpu_usage_metrics['cpu_usage_each_core'] = psutil.cpu_percent(interval=1, percpu=True)

        return cpu_usage_metrics

    def cpu_aggregate(self):
        self._cpu_metrics['cpu_times'] = self.cpu_times()
        self._cpu_metrics['cpu_usage'] = self.cpu_usage()

        return self._cpu_metrics

    @staticmethod
    def memory_virtual():
        memory_virtual_memory_metrics = {}
        vm = psutil.virtual_memory()
        memory_virtual_memory_metrics['total'] = vm.total
        memory_virtual_memory_metrics['available'] = vm.available
        memory_virtual_memory_metrics['free'] = vm.free
        memory_virtual_memory_metrics['used'] = vm.used
        memory_virtual_memory_metrics['percent'] = vm.percent

        return memory_virtual_memory_metrics

    @staticmethod
    def swap_memory():
        memory_swap = {}
        sm = psutil.swap_memory()
        memory_swap['total'] = sm.total
        memory_swap['used'] = sm.used
        memory_swap['free'] = sm.free
        memory_swap['percent'] = sm.percent
        memory_swap['bytes_in'] = sm.sin
        memory_swap['bytes_out'] = sm.sout

        return memory_swap

    def memory_aggregate(self):
        self._memory_metrics['virtual_memory'] = self.memory_virtual()
        self._memory_metrics['swap_memory'] = self.swap_memory()

        return self._memory_metrics

    def memory_partitions(self):
        disk_memory_partitions = {}
        disks = psutil.disk_partitions()

        for disk in disks:
            disk_metrics = {}
            dm = psutil.disk_usage(disk.device)
            disk_metrics['total'] = dm.total
            disk_metrics['used'] = dm.used
            disk_metrics['free'] = dm.free
            disk_metrics['percent'] = dm.percent

            disk_memory_partitions[disk.device] = disk_metrics

        # max data used
        max_data_used = [ data_u['used'] for device, data_u in disk_memory_partitions]
        disk_memory_partitions['max_used'] = max(max_data_used)

        self._disk_metrics = disk_memory_partitions

        return self._disk_metrics

    def network_metrics(self):

        network_data = {}
        nm = psutil.net_io_counters(pernic=False)

        network_data['bytes_sent'] = nm.bytes_sent
        network_data['bytes_recv'] = nm.bytes_recv
        network_data['packets_sent'] = nm.packets_sent
        network_data['packets_recv'] = nm.packets_recv

        self._network_metric = network_data

        return self._network_metric

    def system_metrics(self):
        self._system_metric['cpu'] = self.cpu_aggregate()
        self._system_metric['memory'] = self.memory_aggregate()
        self._system_metric['disk'] = self.memory_partitions()
        self._system_metric['network'] = self.network_metrics()

        return self._system_metric


if __name__ == "__main__":
    metrics = SystemMetrics()
    print(metrics.system_metrics())
