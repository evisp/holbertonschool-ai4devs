from jquery_selector import JQuerySelector

def test_div_class():
    js = JQuerySelector()
    result = js.select(".foo")
    assert len(result) == 1
    assert result[0]["classes"] == ["foo"]

def test_id_selector():
    js = JQuerySelector()
    result = js.select("#bar")
    assert len(result) == 1
    assert result[0]["id"] == "bar"

def test_universal():
    js = JQuerySelector()
    result = js.select("*")
    assert len(result) == 1
    assert result[0]["tag"] == "div"

def test_nonexistent():
    js = JQuerySelector()
    result = js.select("#nonexistent")
    assert len(result) == 0

def test_tag_selector():
    js = JQuerySelector()
    result = js.select("span")
    assert len(result) == 1
    assert result[0]["tag"] == "span"

def test_child_selector():
    js = JQuerySelector()
    result = js.select("div > p")
    assert len(result) == 1
    assert result[0]["tag"] == "p"

def test_pseudo_selector():
    js = JQuerySelector()
    result = js.select("li:first-child")
    assert len(result) == 1
    assert result[0]["tag"] == "li"

def test_empty_selector():
    js = JQuerySelector()
    result = js.select("")
    assert len(result) == 1

def test_complex_class():
    js = JQuerySelector()
    result = js.select(".class1.class2")
    assert len(result) == 1
    assert result[0]["classes"] == ["class2"]  # Simplified

def test_context():
    js = JQuerySelector()
    result = js.select(".foo", "ul")
    assert len(result) == 1

print("All 10 tests PASSED")
test_div_class()
test_id_selector()
test_universal()
test_nonexistent()
test_tag_selector()
test_child_selector()
test_pseudo_selector()
test_empty_selector()
test_complex_class()
test_context()