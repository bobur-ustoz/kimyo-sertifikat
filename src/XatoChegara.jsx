import { Component } from "react";
import { C } from "./theme";
import { xatoYubor } from "./lib/xato";

// Sahifa chizilayotganda xato chiqsa oq ekran o'rniga tushunarli xabar ko'rsatadi va xatoni kod agentiga yuboradi.
export default class XatoChegara extends Component {
  state = { xato: false };
  static getDerivedStateFromError() { return { xato: true }; }
  componentDidCatch(error, info) { xatoYubor(`Sahifa chizilmadi: ${error?.message || error}`, `${error?.stack || ""}\n${info?.componentStack || ""}`); }
  render() {
    if (!this.state.xato) return this.props.children;
    return (
      <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", padding: 24, background: C.bgSoft, fontFamily: "inherit" }}>
        <div style={{ maxWidth: 380, textAlign: "center", background: "#fff", border: `1px solid ${C.border}`, borderRadius: 16, padding: "28px 22px" }}>
          <div style={{ fontSize: 17, fontWeight: 800, color: C.text, marginBottom: 8 }}>Sahifada nosozlik chiqdi</div>
          <p style={{ fontSize: 13.5, color: C.textMid, lineHeight: 1.6, margin: "0 0 18px" }}>Bu sizning aybingiz emas. Xato haqida bizga xabar yuborildi. Sahifani qayta yuklab ko'ring.</p>
          <button onClick={() => window.location.reload()} style={{ padding: "11px 20px", borderRadius: 10, border: "none", background: C.primary, color: "#fff", fontSize: 14, fontWeight: 700, cursor: "pointer", fontFamily: "inherit" }}>Qayta yuklash</button>
          <div style={{ marginTop: 12 }}><a href="/" style={{ fontSize: 12.5, color: C.primary }}>Bosh sahifaga</a></div>
        </div>
      </div>
    );
  }
}
