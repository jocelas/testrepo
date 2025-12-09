# Testing package

Usage:
1. make sure you have **venv**:
<div style="position: relative;">
    <button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)"
                    style="position: absolute; right: 0; top: 0;">
        Copy
    </button>
    <pre><code>sudo apt install python3-venv</code></pre>
</div>
2. clone the repository
<div style="position: relative;">
    <button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)"
                    style="position: absolute; right: 0; top: 0;">
        Copy
    </button>
    <pre><code>git clone https://github.com/jocelas/testrepo.git</code></pre>
</div>

3. Go in the folder
<div style="position: relative;">
    <button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)"
                    style="position: absolute; right: 0; top: 0;">
        Copy
    </button>
    <pre><code>cd testrepo</code></pre>
</div>

4. initialize venv:
<div style="position: relative;">
    <button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)"
                    style="position: absolute; right: 0; top: 0;">
        Copy
    </button>
    <pre><code>python3 -m venv .venv</code></pre>
</div>

5. activate it:
<div style="position: relative;">
    <button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)"
                    style="position: absolute; right: 0; top: 0;">
        Copy
    </button>
    <pre><code>source .venv/bin/activate</code></pre>
</div>

6. install necessary packages using:
<div style="position: relative;">
    <button onclick="navigator.clipboard.writeText(this.nextElementSibling.innerText)"
                    style="position: absolute; right: 0; top: 0;">
        Copy
    </button>
    <pre><code>pip install -e .</code></pre>
</div>

7. try the testing notebook `testing.ipynb`
