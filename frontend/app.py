import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("🧠 Pre-Council NLP → SQL Agent (Streaming UI)")

question = st.text_input("Ask a question", placeholder="Show all customers")

def stream_query(q: str):
    url = "http://127.0.0.1:8000/query/stream"
    with requests.get(url, params={"question": q}, stream=True, timeout=300) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if line:
                yield line.decode("utf-8")

if st.button("Run Query"):
    if not question.strip():
        st.warning("Please enter a question")
        st.stop()

    output_box = st.empty()
    full_text = ""

    with st.spinner("Thinking..."):
        for chunk in stream_query(question):
            full_text += chunk + "\n"
            output_box.code(full_text)

    # 🎬 GSAP animation
    components.html(
        """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
        <div id="card" style="padding:20px;background:#22d3ee;border-radius:12px;font-size:18px;">
            Stream Complete
        </div>
        <script>
          gsap.from("#card", {opacity:0, y:40, duration:1});
        </script>
        """,
        height=120,
    )

    # 🌐 Three.js visualization
    components.html(
        """
        <script src="https://unpkg.com/three@0.152.2/build/three.min.js"></script>
        <canvas id="c"></canvas>
        <script>
          const scene = new THREE.Scene();
          const camera = new THREE.PerspectiveCamera(75, 2, 0.1, 100);
          const renderer = new THREE.WebGLRenderer({canvas: document.getElementById("c")});
          renderer.setSize(400, 200);

          const geometry = new THREE.SphereGeometry(0.4);
          const material = new THREE.MeshBasicMaterial({color: 0x22d3ee});
          const sphere = new THREE.Mesh(geometry, material);
          scene.add(sphere);

          camera.position.z = 3;

          function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.y += 0.02;
            renderer.render(scene, camera);
          }
          animate();
        </script>
        """,
        height=220,
    )
