import psutil


class SystemMetrics:

    def __init__(self):
        self._cpu_metrics = dict()

    def cpu_times(self):

        cpu_times_metrics = {}
        cp_metrics = psutil.cpu_times(percpu=False)
        cpu_times_metrics['user'] = cp_metrics.user
        cpu_times_metrics['system'] = cp_metrics.system
        cpu_times_metrics['idle'] = cp_metrics.idle
        cpu_times_metrics['nice'] = cp_metrics.nice

        return cpu_times_metrics

    def cpu_usage(self):

        cpu_usage_metrics = dict()
        cpu_usage_metrics['cpu_count'] = psutil.cpu_count(logical=True)
        cpu_usage_metrics['cpu_percent'] = psutil.cpu_percent(interval=1)
        cpu_usage_metrics['cpu_usage_each_core'] = psutil.cpu_percent(interval=1, percpu=True)

        return cpu_usage_metrics

    def cpu_aggregate(self):

        self._cpu_metrics['cpu_times'] = self.cpu_times()
        self._cpu_metrics['cpu_usage'] = self.cpu_usage()

        return self._cpu_metrics

    def memory_virtual(self):

        memory_virtual_memory_metrics = {}
        vm = psutil.virtual_memory()
        memory_virtual_memory_metrics['total'] = vm.total
        memory_virtual_memory_metrics['available'] = vm.available
        memory_virtual_memory_metrics['free'] = vm.free
        memory_virtual_memory_metrics['used'] = vm.used
        memory_virtual_memory_metrics['percent'] = vm.percent

        return memory_virtual_memory_metrics

    def swap_memory(self):

        memory_swap = {}
        sm = psutil.swap_memory()
        memory_swap['total'] = sm.total
        memory_swap['used'] = sm.used
        memory_swap['free'] = sm.free
        memory_swap['percent'] = sm.percent
        memory_swap['bytes_in'] = sm.sin
        memory_swap['bytes_out'] = sm.sout

        return memory_swap


if __name__ == "__main__":
    metrics = SystemMetrics()
    print(metrics.swap_memory())
