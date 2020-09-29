class IterationHit:

    def __init__(self, iteration):
        self.iteration = iteration
        self.repetitions = 0
        self.sample_num = 0
        self.hsp_positive = 0
        self.iteration_query_len = 0
        self.hit_def = ''
        self.get_info()

    def get_info(self):

        self.iteration_query_len = float(self.iteration.find('Iteration_query-len').text)
        iteration_def = self.iteration.find('Iteration_query-def').text.split('-')
        self.sample_num = int(iteration_def[0])
        self.repetitions = int(iteration_def[1])

        iteration_hits = self.iteration.find('Iteration_hits').findall('Hit')
        first_hit = 0

        for hit in iteration_hits:
            hit_num = hit.find('Hit_num').text
            if hit_num == '1':
                first_hit = hit
                break

        self.hit_def = first_hit.find('Hit_def').text
        self.hit_def = ' '.join(self.hit_def.split(' ')[0:2])
        self.hsp_positive = float(first_hit.find('Hit_hsps').find('Hsp').find('Hsp_positive').text)

    def get_result(self):
        if self.hsp_positive / self.iteration_query_len > 0.9:
            return self.sample_num, self.hit_def, self.repetitions
        else:
            return self.sample_num, "< 90%"
