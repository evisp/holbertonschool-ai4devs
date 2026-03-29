# Cross-Language Specification - jQuery Selector Engine

## Algorithm
Given a CSS selector string and context DOM element(s), find all matching descendant elements using a compiled parser that handles complex combinators (>, +, ~) and pseudo-classes.

## Inputs
- selector: CSS selector string (e.g. "div.foo > ul li:first-child")
- context: DOM element, NodeList, or jQuery collection (default: document)

## Outputs
- Array of matching DOM elements in document order

## Edge Cases
- Invalid selector syntax
- Empty context/no matches  
- Detached DOM nodes
- Universal selector "*"
- Disconnected context nodes

## Test Cases
- "div > p" in simple HTML → [2 paragraph nodes]
- ".class1.class2" → [3 elements with both classes]
- "ul li:first-child" → [first li per ul parent]
- "#nonexistent" → []
- "*" in empty div → []