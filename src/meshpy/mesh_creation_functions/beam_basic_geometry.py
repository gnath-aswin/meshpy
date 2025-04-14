# The MIT License (MIT)
#
# Copyright (c) 2018-2025 MeshPy Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""DEPRECATED: Use `beam_line`, `beam_arc`, and `beam_helix` instead.

This file will be removed in a future release.
"""

import warnings as _warnings

_warnings.warn(
    "beam_basic_geometry is deprecated and will be removed in a future release. "
    "Please use beam_line, beam_arc, and beam_helix instead.",
    DeprecationWarning,
    stacklevel=2,
)

from .beam_arc import (
    create_beam_mesh_arc_at_node as _create_beam_mesh_arc_at_node,
)
from .beam_arc import (
    create_beam_mesh_arc_segment_2d as _create_beam_mesh_arc_segment_2d,
)
from .beam_arc import (
    create_beam_mesh_arc_segment_via_axis as _create_beam_mesh_arc_segment_via_axis,
)
from .beam_arc import (
    create_beam_mesh_arc_segment_via_rotation as _create_beam_mesh_arc_segment_via_rotation,
)
from .beam_helix import create_beam_mesh_helix as _create_beam_mesh_helix
from .beam_line import (
    create_beam_mesh_line as _create_beam_mesh_line,
)
from .beam_line import (
    create_beam_mesh_line_at_node as _create_beam_mesh_line_at_node,
)

__all__ = [
    "create_beam_mesh_line",
    "create_beam_mesh_line_at_node",
    "create_beam_mesh_arc_segment_via_rotation",
    "create_beam_mesh_arc_segment_via_axis",
    "create_beam_mesh_arc_segment_2d",
    "create_beam_mesh_arc_at_node",
    "create_beam_mesh_helix",
]

# Re-export under original names
create_beam_mesh_line = _create_beam_mesh_line
create_beam_mesh_line_at_node = _create_beam_mesh_line_at_node
create_beam_mesh_arc_segment_via_rotation = _create_beam_mesh_arc_segment_via_rotation
create_beam_mesh_arc_segment_via_axis = _create_beam_mesh_arc_segment_via_axis
create_beam_mesh_arc_segment_2d = _create_beam_mesh_arc_segment_2d
create_beam_mesh_arc_at_node = _create_beam_mesh_arc_at_node
create_beam_mesh_helix = _create_beam_mesh_helix
