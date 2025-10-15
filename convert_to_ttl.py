#!/usr/bin/env python3
"""
Convert OWL (RDF/XML) files to Turtle (TTL) format
"""

import sys
from pathlib import Path

try:
    from rdflib import Graph
except ImportError:
    print("Error: rdflib not installed. Install it with: pip install rdflib")
    sys.exit(1)

def convert_owl_to_ttl(owl_file, ttl_file=None):
    """
    Convert an OWL file (RDF/XML format) to Turtle format
    
    Args:
        owl_file (str): Path to the input OWL file
        ttl_file (str): Path to the output TTL file (optional)
    """
    owl_path = Path(owl_file)
    
    if not owl_path.exists():
        print(f"Error: File {owl_file} not found")
        return False
    
    # Generate output filename if not provided
    if ttl_file is None:
        ttl_file = owl_path.with_suffix('.ttl')
    
    try:
        # Create a new graph and parse the OWL file
        g = Graph()
        print(f"Parsing {owl_file}...")
        g.parse(owl_file, format='xml')
        
        # Serialize to Turtle format
        print(f"Converting to Turtle format...")
        ttl_content = g.serialize(format='turtle')
        
        # Write to file
        with open(ttl_file, 'w', encoding='utf-8') as f:
            f.write(ttl_content)
        
        print(f"Successfully converted {owl_file} to {ttl_file}")
        return True
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_ttl.py <owl_file> [output_file]")
        print("Example: python convert_to_ttl.py template.owl template.ttl")
        sys.exit(1)
    
    owl_file = sys.argv[1]
    ttl_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_owl_to_ttl(owl_file, ttl_file)