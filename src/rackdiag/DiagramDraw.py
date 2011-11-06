# -*- coding: utf-8 -*-
#  Copyright 2011 Takeshi KOMIYA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import blockdiag.DiagramDraw
from blockdiag.utils import XY


class DiagramDraw(blockdiag.DiagramDraw.DiagramDraw):
    def _draw_elements(self, **kwargs):
        frame = self.metrics.frame
        self.drawer.rectangle(frame, outline=self.diagram.linecolor)

        for i in range(self.diagram.rackheight):
            box = self.metrics.racknumber(i)
            number = u"%d" % (i + 1)
            self.drawer.textarea(box, number, halign='right')

        super(DiagramDraw, self)._draw_elements(**kwargs)


from DiagramMetrics import DiagramMetrics
DiagramDraw.set_metrics_class(DiagramMetrics)
