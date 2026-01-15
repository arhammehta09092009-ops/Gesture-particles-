<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Einstein–Rosen Bridge (Theoretical)</title>
  <style>
    body { margin: 0; overflow: hidden; background: black; }
    canvas { display: block; }
  </style>
</head>
<body>

<script src="https://cdn.jsdelivr.net/npm/three@0.155/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.155/examples/js/controls/OrbitControls.js"></script>

<script>
  // Scene
  const scene = new THREE.Scene();

  // Camera
  const camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.set(0, 10, 25);

  // Renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // Controls
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;

  // Light
  const light = new THREE.PointLight(0xffffff, 1);
  light.position.set(10, 20, 10);
  scene.add(light);

  const ambient = new THREE.AmbientLight(0x404040);
  scene.add(ambient);

  // Wormhole geometry (embedding diagram)
  const rs = 2; // Schwarzschild radius
  const segments = 200;
  const geometry = new THREE.BufferGeometry();

  const vertices = [];

  for (let i = 0; i < segments; i++) {
    const r = rs + i * 0.05;
    const z = 2 * Math.sqrt(rs * (r - rs));

    for (let theta = 0; theta <= Math.PI * 2; theta += Math.PI / 30) {
      const x = r * Math.cos(theta);
      const y = r * Math.sin(theta);

      vertices.push(x, y, z);
      vertices.push(x, y, -z);
    }
  }

  geometry.setAttribute(
    'position',
    new THREE.Float32BufferAttribute(vertices, 3)
  );

  const material = new THREE.PointsMaterial({
    color: 0x00ffff,
    size: 0.05
  });

  const wormhole = new THREE.Points(geometry, material);
  scene.add(wormhole);

  // Animation loop
  function animate() {
    requestAnimationFrame(animate);
    wormhole.rotation.y += 0.001;
    controls.update();
    renderer.render(scene, camera);
  }

  animate();

  // Resize handling
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
</script>

</body>
</html>
