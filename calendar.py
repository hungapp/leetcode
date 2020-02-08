Event = collections.namedtuple('Event', ('start', 'finish'))
#is_start is bool
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):
  E = ([Endpoint(event.start, True)] for event in A + [Endpoint(event.stop, False)] for event in A)
  E.sort(key=lambda e: (e.time, not e.is_start)) # start time comes first - True - 1
  max_num_simultaneous_events, num_simultaneous_events = 0, 0
  for e in E:
    if e.is_start:
      num_simultaneous_events += 1
      max_num_simultaneous_events = max(max_num_simultaneous_events, num_simultaneous_events)
    else:
      num_simultaneous_events -= 1
  return max_num_simultaneous_events


