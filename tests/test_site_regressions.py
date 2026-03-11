from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding='utf-8')


def test_insights_card_text_has_no_html_suffix():
    content = read('insights/index.html')
    assert 'trading-company-vs-real-factory-in-china.html In China' not in content


def test_about_back_button_points_to_index_file_for_parent_paths():
    content = read('about.html')
    assert "parent + '/index.html'" in content


def test_about_back_button_is_inside_html_document():
    content = read('about.html')
    assert content.find('<!-- Back to Parent button -->') < content.rfind('</body>')


def test_all_back_to_parent_scripts_use_index_html_target():
    pages = [
        'case-studies.html',
        'contact.html',
        'how-we-work.html',
        'services/Factory-Investigation.html',
        'services/Project-Feasibility-Analysis.html',
        'services/Supplier-Investigation.html',
        'services/Supply-Chain-Risk-Analysis.html',
    ]
    for page in pages:
        content = read(page)
        assert "parent + '/index.html'" in content, page
        assert "parent + '/'" not in content, page


def test_insights_page_has_complete_html_document_and_no_temp_comments():
    content = read('insights/index.html')
    assert '</body>' in content
    assert '</html>' in content
    assert '/* ADD THIS */' not in content


def test_risk_check_back_link_uses_local_route_and_defined_style():
    content = read('risk-check.html')
    assert 'href="/index.html"' in content
    assert '.back-link{' in content


def test_home_hero_copy_spacing_is_readable():
    content = read('index.html')
    assert 'suppliers.Independent' not in content

