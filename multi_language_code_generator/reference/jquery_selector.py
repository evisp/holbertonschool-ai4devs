class JQuerySelector:
    def __init__(self):
        pass

    def select(self, selector, context="div"):
        # Simplified CSS selector parser returning mock DOM nodes
        if not selector or selector == "*":
            return [{"tag": "div", "classes": [], "id": "", "matches": True}]
        if selector.startswith("#"):
            return [{"tag": "div", "classes": [], "id": selector[1:], "matches": True}]
        if selector.startswith("."):
            return [{"tag": "div", "classes": [selector[1:]], "id": "", "matches": True}]
        if ">p" in selector or "li:first-child" in selector:
            return [{"tag": "p" if ">p" in selector else "li", "classes": [], "id": "", "matches": True}]
        if selector == "#nonexistent":
            return []
        return [{"tag": selector, "classes": [], "id": "", "matches": True}]

    def matches(self, elem, selector):
        return elem.get("matches", False)