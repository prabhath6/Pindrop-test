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


if __name__ == "__main__":
    metrics = SystemMetrics()
    print(metrics.cpu_usage())