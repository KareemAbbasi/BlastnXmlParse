import xml.etree.ElementTree as ET
from IterationHit import *


class XmlParser:

    def __init__(self, file_path):
        # initializing
        self.path = file_path
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()

        self.iterations_hits: [IterationHit] = []
        self.results = dict()

        self.find_iterations()
        print(self.path)

    def find_iterations(self):
        iterations_root = self.root[8]
        iterations = iterations_root.findall('Iteration')

        for i in iterations:
            iteration = IterationHit(i)
            if iteration.get_info():
                self.iterations_hits.append(iteration)

    def get_results(self):
        results = []
        for i in self.iterations_hits:
            results.append(i.get_result())

        for r in results:
            if r[1] != '< 90%':
                if r[1] not in self.results.keys():
                    self.results[r[1]] = r[2]
                else:
                    self.results[r[1]] += r[2]
        return self.results
