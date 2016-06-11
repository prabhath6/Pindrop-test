import psutil


class SystemMetrics:

    def cpu_metrics(self):

        cpu_times_metrics = {}
        cp_metrics = psutil.cpu_times(percpu=False)
        cpu_times_metrics['user'] = cp_metrics.user
        cpu_times_metrics['system'] = cp_metrics.system
        cpu_times_metrics['idle'] = cp_metrics.idle
        cpu_times_metrics['nice'] = cp_metrics.nice

        return cpu_times_metrics


if __name__ == "__main__":
    metrics = SystemMetrics()
    print(metrics.cpu_metrics())