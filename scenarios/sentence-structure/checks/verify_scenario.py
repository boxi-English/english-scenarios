"""Offline checks for the first text-first English scenario."""

from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).parents[1]
data=json.loads((ROOT/'fixture.json').read_text())
assert data['item_id']=='counterfactual-1'
assert len(data['segments'])==2
assert data['expected_choice']==1
assert 'had known' in data['segments'][1]['text']
assert 'would have called' in data['segments'][1]['text']
assert set(data['response_dimensions']) == {'form','time_reference','communicative_fit'}
assert data['transfer_prompt'].startswith('If I had seen')
print('PASS: scenario has context, prediction, inspectable feedback dimensions, revision, and transfer')
