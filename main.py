from manim import *
from manim_editor import PresentationSectionType

def create_item(s):
  dot = Dot()
  return VGroup(dot, s.next_to(dot, RIGHT))

class A_Title(Scene):
  def construct(self):
    self.next_section("A", PresentationSectionType.NORMAL)
    title = Text("Proof-Carrying Data from\nAccumulation Schemes", font_size=60)
    authors = Text("Bünz, Chiesa, Mishra, Spooner", font_size=30).next_to(title, DOWN)
    self.add(title, authors)
    self.wait()

class B_IVC(Scene):
   def construct(self):
      self.next_section("B", PresentationSectionType.NORMAL)
      square = Square().shift(4*LEFT)
      left_arrow = Arrow().next_to(square, LEFT)
      z = MathTex(r"z_0").next_to(left_arrow, UP)
      pis = []
      top_arrow = Arrow(start=ORIGIN + 2*UP, end=ORIGIN).next_to(square, UP)
      w = MathTex("w_0").next_to(top_arrow, LEFT)
      right_arrow = Arrow().next_to(square, RIGHT)
      arrows=[right_arrow]
      z1 = MathTex(r"z_1").next_to(right_arrow, UP)
      pi1 = MathTex(r"\pi_1", color=BLACK).next_to(right_arrow, DOWN)
      pis.append(pi1)
      F = MathTex("F").move_to(square)
      g = Group(square, z, w, F, left_arrow, top_arrow)
      self.play(FadeIn(g))

      self.next_section("B.1", PresentationSectionType.SUB_NORMAL)      
      F1 = MathTex(r"F(z_0, w_0)").move_to(square).set_fill(BLACK)
      zz,ww = z.copy(), w.copy()
      self.remove(left_arrow, top_arrow)
      self.play(zz.animate.shift(2*RIGHT), ww.animate.shift(2*DOWN), FadeIn(F1), square.animate.set_fill(WHITE, opacity=1.0))
      self.remove(zz, ww)

      self.play(FadeTransform(F1, z1), GrowArrow(right_arrow), square.animate.set_fill(BLACK, opacity=0))

      self.next_section("B.2", PresentationSectionType.SUB_NORMAL)      
      square2 = Square().next_to(right_arrow, RIGHT)
      F2 = MathTex("F").move_to(square2)
      top_arrow2 = Arrow(start=ORIGIN + 2*UP, end=ORIGIN).next_to(square2, UP)
      w2 = MathTex("w_1").next_to(top_arrow2, LEFT)
      g2 = Group(square2, F2, w2, top_arrow2)
      self.play(FadeIn(g2))
      self.remove(top_arrow2)
      right_arrow.set_color(BLACK)

      F3 = MathTex(r"F(z_1, w_1)").move_to(square2).set_fill(BLACK)
      zz,ww = z1.copy(), w2.copy()
      self.play(zz.animate.shift(2*RIGHT), ww.animate.shift(2*DOWN), FadeIn(F3), square2.animate.set_fill(WHITE, opacity=1.0))
      self.remove(zz, ww)

      right_arrow2 = Arrow().next_to(square2, RIGHT)
      arrows.append(right_arrow2)
      z2 = MathTex(r"z_2").next_to(right_arrow2, UP)
      pi2 = MathTex(r"\pi_2", color=BLACK).next_to(right_arrow2, DOWN)
      pis.append(pi2)
      self.play(FadeTransform(F3, z2), GrowArrow(right_arrow2), square2.animate.set_fill(BLACK, opacity=0))

      dots = Text("...").next_to(right_arrow2, RIGHT).shift(0.3*DOWN)
      self.play(Write(dots))

      self.next_section("B.3", PresentationSectionType.SUB_NORMAL)      
      gg = Group(square, z, w, pi1, square2, z1, w2, z2, pi2, dots, F, F2, right_arrow, right_arrow2)
      self.play(gg.animate.shift(9.8*LEFT))
      right_arrow2.set_color(BLACK)

      right_arrow = Arrow().next_to(dots, RIGHT).shift(0.3*UP)
      arrows.append(right_arrow)
      z = MathTex(r"z_{t-1}").next_to(right_arrow, UP)
      pi = MathTex(r"\pi_{t-1}", color=BLACK).next_to(right_arrow, DOWN)
      pis.append(pi)
      square = Square().next_to(right_arrow, RIGHT)
      F = MathTex("F").move_to(square)
      top_arrow = Arrow(start=ORIGIN + 2*UP, end=ORIGIN).next_to(square, UP)
      w = MathTex("w_{t-1}").next_to(top_arrow, LEFT).shift(0.4*RIGHT)
      g = Group(square, F, w, top_arrow, right_arrow, z, pi)
      self.play(FadeIn(g))
      self.remove(right_arrow, top_arrow)

      F2 = MathTex(r"F(z_{t-1}, w_{t-1})", font_size=30).move_to(square).set_fill(BLACK)
      zz,ww = z.copy(), w.copy()
      self.play(zz.animate.shift(2*RIGHT), ww.animate.shift(2*DOWN), FadeIn(F2), square.animate.set_fill(WHITE, opacity=1.0))
      self.remove(zz, ww)

      right_arrow2 = Arrow().next_to(square, RIGHT)
      arrows.append(right_arrow2)
      zt = MathTex(r"z_t").next_to(right_arrow2, UP)
      pt = MathTex(r"\pi_t", color=BLACK).next_to(right_arrow2, DOWN)
      pis.append(pt)

      self.play(FadeTransform(F2, zt), GrowArrow(right_arrow2), square.animate.set_fill(BLACK, opacity=0))

      self.next_section("B.4", PresentationSectionType.SUB_NORMAL)      
      framebox1 = SurroundingRectangle(zt, buff = .1)
      fb = SurroundingRectangle(pt, buff = .1, color=BLACK)
      pis.append(fb)
      self.play(Create(framebox1))

      self.next_section("B.5", PresentationSectionType.SUB_NORMAL)      
      gg.add(square, z, pi, w, F, zt, pt, framebox1, fb, right_arrow2)
      for arrow in arrows:
        arrow.set_color(WHITE)
      self.play(gg.animate.scale(0.6).move_to(1.8*UP))
      framebox2 = SurroundingRectangle(gg, buff = .2, color=WHITE)
      label = Text("t-step (nondeterministic) computation", font_size=30).next_to(framebox2, UP)
      self.play(Create(framebox2), Write(label))

      self.next_section("B.6", PresentationSectionType.SUB_NORMAL)      
      self.add(gg.copy())
      self.play(gg.animate.move_to(2*DOWN))
      for pi in pis:
        pi.set_color(BLUE)
      framebox2 = SurroundingRectangle(gg, buff = .2, color=WHITE)
      label2 = Text("IVC [Val08]", font_size=32).next_to(framebox2, UP)
      self.play(Create(framebox2), Write(label2))

class C_IVCApplications(Scene):
  def construct(self):
    self.next_section("C", PresentationSectionType.NORMAL)
    title = Text("Applications of IVC/PCD").move_to(3*UP)
    self.add(title)
    self.wait()
 
    self.next_section("C.1", PresentationSectionType.SUB_NORMAL)
    item1 = create_item(Text("SNARKs with small space and time complexity [BCCT13]", font_size=30)).next_to(title, 4.5*DOWN)
    self.add(item1)
    self.wait()

    self.next_section("C.2", PresentationSectionType.SUB_NORMAL)
    item2 = create_item(Text("Succinct Blockchains (Coda [MS18], [KB20])", font_size=30)).next_to(item1, 2.5*DOWN).align_to(item1, LEFT)
    self.add(item2)
    self.wait()

    self.next_section("C.3", PresentationSectionType.SUB_NORMAL)
    item3 = create_item(Text("Verifiable Delay Functions [BBBF19]", font_size=30)).next_to(item2, 2.5*DOWN).align_to(item2, LEFT)
    self.add(item3)
    self.wait()

    self.next_section("C.4", PresentationSectionType.SUB_NORMAL)
    item4 = create_item(Text("...", font_size=30)).next_to(item3, 2.5*DOWN).align_to(item3, LEFT)
    self.add(item4)
    self.wait()

class D_IVCConstructions(Scene):
  def construct(self):
    self.next_section("D", PresentationSectionType.NORMAL)
    title = Text("How construct IVC/PCD?").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("D.1", PresentationSectionType.SUB_NORMAL)
    item_1 = create_item(Text("[BCCT13]: SNARKs with succinct (polylog) verification", font_size=30)).next_to(title, 4.5*DOWN)
    self.add(item_1)
    self.wait()

    self.next_section("D.2", PresentationSectionType.SUB_NORMAL)
    item_2 = create_item(Text("[COS20]: SNARKs with sublinear verification", font_size=30)).next_to(item_1, 2.5*DOWN).align_to(item_1, LEFT)
    self.add(item_2)
    self.wait()

    self.next_section("D.3", PresentationSectionType.SUB_NORMAL)
    framebox = SurroundingRectangle(VGroup(item_1, item_2), buff = .1, color=RED)
    warning = Text("Sublinear verification requirement restricts the SNARKs we can use! 😔", font_size=20, color=RED).next_to(framebox, UP)
    self.play(Create(framebox), FadeIn(warning))

    self.next_section("D.4", PresentationSectionType.SUB_NORMAL)
    solution = Text("[BGH19] suggests how to overcome this limitation!", font_size = 30).move_to(2*DOWN).align_to(item_1, LEFT)
    self.add(solution)
    self.wait()

    self.next_section("D.5", PresentationSectionType.SUB_NORMAL)
    solution_item_1 = create_item(MarkupText("A novel approach to obtain IVC from a specific SNARK with <span foreground='yellow'>linear verification</span>", font_size = 21)).next_to(solution, 2*DOWN).align_to(solution, LEFT)
    self.add(solution_item_1)
    self.remove(framebox)
    framebox = SurroundingRectangle(VGroup(solution, solution_item_1), buff = .1, color=GREEN)
    good_news = Text("We can use SNARKs whose verifier is not sublinear! 🙂", font_size=20, color=GREEN).next_to(framebox, UP)
    self.play(Create(framebox), FadeIn(good_news))
    self.wait()

    self.next_section("D.6", PresentationSectionType.SUB_NORMAL)
    solution_item_2 = create_item(Text("But they don’t provide a detailed construction or a security proof...", font_size = 21, color=RED)).next_to(solution_item_1, 1.5*DOWN).align_to(solution, LEFT)
    self.add(solution_item_2)
    self.remove(framebox)
    self.wait()

class E_ASIntro(Scene):
  def construct(self):
    self.next_section("E", PresentationSectionType.NORMAL)
    title = Text("Accumulation Schemes: Overview").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("E.1", PresentationSectionType.SUB_NORMAL)
    item_1 = Tex(r"Let $q_1,q_2$, \dots be an infinite stream, with $q_i \in \mathcal{X}$", font_size=30).move_to(3*LEFT).shift(2*UP)
    item_2 = create_item(Tex(r"At time $i$, the prover receives $(q_i$, acc$_{i-1})$ and computes acc$_i$", font_size=30)).next_to(item_1, 1.5*DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Tex(r"The verifier checks that acc$_{i-1}$ and $q_i$ were correctly accumulated into acc$_i$", font_size=30)).next_to(item_2, 1.5*DOWN).align_to(item_1, LEFT)
    item_4 = create_item(Tex(r"At any time $t$, the decider can validate acc$_t$, i.e. $\forall i \in [t], \Phi(q_i) = 1$", font_size=30)).next_to(item_3, 1.5*DOWN).align_to(item_1, LEFT)
    self.add(item_1, item_2, item_3, item_4)
    self.wait()

    self.next_section("E.2", PresentationSectionType.SUB_NORMAL)
    item_5 = Tex(r"Trivial solution: $(\mathbb{P} = \emptyset, \mathbb{V} = \Phi, \mathbb{D} = \emptyset)$", font_size=40).next_to(item_4, 3.5*DOWN).align_to(item_1, LEFT)
    self.add(item_5)
    self.wait()

    self.next_section("E.3", PresentationSectionType.SUB_NORMAL)
    item_6 = Tex(r"However", font_size=30).next_to(item_5, 1.5*DOWN).align_to(item_1, LEFT)
    item_7 = create_item(Tex(r"The verifier should be (much) more efficient than $\Phi$", font_size=30, color=YELLOW)).next_to(item_6, 1.5*DOWN).align_to(item_1, LEFT)
    item_8 = create_item(Tex(r"The size of an accumulator should not grow over time", font_size=30, color=YELLOW)).next_to(item_7, 1.5*DOWN).align_to(item_1, LEFT)

    self.add(item_6, item_7, item_8)
    self.wait()

class F_PESnark(Scene):
  def construct(self):
    self.next_section("F", PresentationSectionType.NORMAL)      
    title = Text("Predicate-efficient SNARKs").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("F.1", PresentationSectionType.SUB_NORMAL)      
    definition = Tex(r"A SNARK $(P, V)$ is predicate-efficient wrt a predicate $\Phi$ if:", font_size=34).move_to(2*LEFT).shift(2*UP)
    item_1 = create_item(Tex("Runs a", " fast ", r"inner verifier $V_{pe}$ to produce a bit $b$ and", " query set $Q$", font_size=30).set_color_by_tex("fast", YELLOW).set_color_by_tex("set", RED)).next_to(definition, 1.5*DOWN).align_to(definition, LEFT)
    item_2 = create_item(Tex(r"Accepts iff $b = 1$ and $\forall q \in Q, \Phi(q) = 1$", font_size=30)).next_to(item_1, 1.5*DOWN).align_to(item_1, LEFT)

    self.add(definition, item_1, item_2)
    self.wait()

    self.next_section("F.2", PresentationSectionType.SUB_NORMAL)      
    vpe = MathTex(r"V_{pe}")
    vpe = VGroup(vpe, SurroundingRectangle(vpe)).shift(2*LEFT, 3.5*DOWN)
    phi = Tex(r"$\Phi$")
    fb = SurroundingRectangle(phi, color = RED)
    phi = VGroup(phi, fb)
    dot1 = Dot().scale(0.5).next_to(phi, DOWN)
    dot2 = Dot().scale(0.5).next_to(dot1, DOWN)
    dot3 = Dot().scale(0.5).next_to(dot2, DOWN)
    phi2 = phi.copy().next_to(dot3, DOWN)
    gand = Tex(r"$\land$").next_to(dot3, 6*RIGHT + 4*DOWN)

    line1 = Line(start = vpe.get_center() + [0, vpe.height/2, 0], end = vpe.get_center() + [0, 5*vpe.height, 0])
    arrow_1 = Arrow(start = line1.get_end(), end=phi.get_center() - [phi.width/2, 0, 0] )
    q1 = MathTex(r"q_1").next_to(arrow_1, DOWN)
    arrow_2 = arrow_1.copy().shift(2*DOWN)
    q2 = MathTex(r"q_n").next_to(arrow_2, DOWN)
    arrow_b = Arrow(start = vpe, end = gand)
    b = Tex(r"b").next_to(arrow_b, DOWN)
    arrow_3 = Arrow(start = phi, end = gand)
    arrow_4 = Arrow(start = phi2, end = gand)
    circuit = VGroup(vpe, phi, dot1, dot2, dot3, phi2, gand, line1, arrow_1, arrow_2, arrow_b, arrow_3, arrow_4, q1, q2, b).scale(0.9).shift(2*RIGHT)

    fb = SurroundingRectangle(circuit, color=GREEN)
    v = MathTex(r"V(x, \pi) \equiv", color=GREEN).next_to(circuit, LEFT)
    self.play(Write(fb), Write(v))
    self.wait()

    self.next_section("F.2", PresentationSectionType.SUB_NORMAL)      
    self.play(FadeTransform(item_1.copy(), circuit))

class G_PESnarkAS(Scene):
  def construct(self):
    self.next_section("G", PresentationSectionType.NORMAL)      
    title = Text("Accumulation for PE SNARKs").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("G.1", PresentationSectionType.SUB_NORMAL)      
    thm_tex = Tex(r"Suppose a SNARK is predicate-efficient wrt a predicate $\Phi$.\\",
             r"If $\Phi$ has $AS_\Phi = (\mathbb{P}_\Phi, \mathbb{V}_\Phi, \mathbb{D}_\Phi)$, ",
              r"then the SNARK has $AS_{ARG} = (\mathbb{P}, \mathbb{V}, \mathbb{D})$", font_size=30).shift(UP)    
    thm_fb = SurroundingRectangle(thm_tex, color=WHITE, buff=0.3)
    thm_label = Text("Theorem 2", font_size=20).next_to(thm_fb, UP).shift(4.4*LEFT)
    thm = VGroup(thm_fb, thm_label, thm_tex)
    self.add(thm)
    self.wait()

    self.next_section("G.2", PresentationSectionType.SUB_NORMAL)      
    item_1 = create_item(Tex(r"$\mathbb{P}$ runs $(b, Q) \leftarrow V_{pe}(x, \pi)$. Then outputs $a^* \leftarrow \mathbb{P}_\Phi(Q, a)$", font_size=30)).shift(DOWN + 5*LEFT)
    item_2 = create_item(Tex(r"$\mathbb{V}$ runs $(b, Q) \leftarrow V_{pe}(x, \pi)$. Checks that $b = 1$ and outputs $\mathbb{V}_\Phi(Q, a, a^*)$", font_size=30)).next_to(item_1, DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Tex(r"At step $t, \mathbb{D}$ outputs $\mathbb{D}_\Phi(a_t)$", font_size=30)).next_to(item_2, DOWN).align_to(item_1, LEFT)

    self.add(item_1, item_2, item_3)
    self.wait()

class H_PopularSnark(Scene):
  def construct(self):
    self.next_section("H", PresentationSectionType.NORMAL)
    title = Text("Ingredients for SNARKs").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("H.1", PresentationSectionType.SUB_NORMAL)
    item_1 = create_item(Text("A Polynomial IOP / AHP", font_size=30)).move_to(3*LEFT).shift(1.5*UP)
    item_2 = create_item(Text("A Polynomial Commitment (PC) scheme", font_size=30)).next_to(item_1, DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Text("A Compiler", font_size=30)).next_to(item_2, DOWN).align_to(item_1, LEFT)
    self.add(item_1, item_2, item_3)
    self.wait()

    self.next_section("H.2", PresentationSectionType.SUB_NORMAL)
    compiler_header = Text("Compiler", font_size=30)
    compiler_schemes = Text("[BBB19], [CHMMVW20]", font_size=12).next_to(compiler_header, DOWN)
    compiler_text = VGroup(compiler_header, compiler_schemes)
    compiler_fb = SurroundingRectangle(compiler_text, buff=0.1, color=WHITE, corner_radius=0.1)
    compiler = VGroup(compiler_text, compiler_fb).shift(RIGHT + 2 * DOWN)

    iop_header = Text("IOP", font_size=30)
    iop_schemes = Text("Sonic, PLONK, Marlin", font_size=12).next_to(iop_header, DOWN)
    iop_text = VGroup(iop_header, iop_schemes)
    iop_fb = SurroundingRectangle(iop_text, buff=0.1, color=WHITE, corner_radius=0.1)
    iop = VGroup(iop_text, iop_fb).align_to(title, LEFT).shift(DOWN)

    pc_header = Text("PC", font_size=30)
    pc_schemes = Text("[KZG10], [BBB19], Halo", font_size=12).next_to(pc_header, DOWN)
    pc_text = VGroup(pc_header, pc_schemes)
    pc_fb = SurroundingRectangle(pc_text, buff=0.1, color=WHITE, corner_radius=0.1)
    pc = VGroup(pc_text, pc_fb).next_to(iop, 3*DOWN)

    arrow_1 = Arrow(start = iop.get_center() + [iop.width/2, 0, 0], end=compiler.get_center() - [compiler.width/2, -0.2, 0] )
    arrow_2 = Arrow(start = pc.get_center() + [pc.width/2, 0, 0], end=compiler.get_center() - [compiler.width/2, 0.2, 0] )

    snark_box = Rectangle()
    snark_text = Text("SNARK").move_to(snark_box)
    snark = VGroup(snark_box, snark_text).move_to(2.2*LEFT + 2*DOWN)

    self.play(FadeTransform(item_1.copy(), iop))
    self.wait()

    self.next_section("H.3", PresentationSectionType.SUB_NORMAL)
    self.play(FadeTransform(item_2.copy(), pc))

    self.next_section("H.4", PresentationSectionType.SUB_NORMAL)
    self.play(FadeTransform(item_3.copy(), compiler))

    self.next_section("H.5", PresentationSectionType.SUB_NORMAL)
    self.play(GrowArrow(arrow_1), GrowArrow(arrow_2))

    self.next_section("H.6", PresentationSectionType.SUB_NORMAL)
    self.play(FadeTransform(VGroup(pc, iop, compiler, arrow_1, arrow_2), snark))

    self.next_section("H.7", PresentationSectionType.SUB_NORMAL)
    txt = Text("PE wrt PC.Check!", color=YELLOW, font_size=20).next_to(snark_text, DOWN)
    self.add(txt)
    self.wait()

    self.next_section("H.8", PresentationSectionType.SUB_NORMAL)
    implies = Tex(r"$\Rightarrow$", font_size=80).next_to(snark, RIGHT).align_to(snark.get_center(), ORIGIN)
    self.add(implies)
    line_1 = Text("Accumulation Scheme", font_size=24).next_to(implies, RIGHT).align_to(implies.get_center(), ORIGIN)
    line_2 = Text("for SNARK", font_size=24).next_to(line_1, DOWN)
    self.add(line_1, line_2)

    fb = SurroundingRectangle(VGroup(snark, line_1), color=GREEN, buff=0.3)
    self.add(fb, Text("Thorem 2", color=GREEN, font_size=20).next_to(fb, DOWN).align_to(title, LEFT))
    self.wait()

class I_PC(Scene):
  def construct(self):
    self.next_section("I", PresentationSectionType.NORMAL)
    title = Text("Polynomial Commitments 101").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("I.1", PresentationSectionType.NORMAL)
    item_1 = Tex(r"Let $f$ be a polynomial $\in \mathbb{F}_p^{\le d}[X]$", font_size=30).move_to(3*LEFT).shift(1.5*UP)
    item_2 = create_item(Tex(r"The sender S produces a commitment $C$ to $f$", font_size=30)).next_to(item_1, DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Tex(r"The receiver R sends an evaluation point $z$", font_size=30)).next_to(item_2, DOWN).align_to(item_1, LEFT)
    item_4 = create_item(Tex("S reveals $v \leftarrow f(z)$ and attaches a proof $\pi$", font_size=30)).next_to(item_3, DOWN).align_to(item_1, LEFT)
    item_5 = create_item(Tex("R verifies that $C, z, v, \pi$ are ``consistent'', i.e. $f(z) = v$", font_size=30)).next_to(item_4, DOWN).align_to(item_1, LEFT)
    self.add(item_1, item_2, item_3, item_4, item_5)
    self.wait()

class J_PCDL(Scene):
  def construct(self):
    self.next_section("J", PresentationSectionType.NORMAL)
    title = Tex(r"PC$_{DL}$: Overview").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("J.1", PresentationSectionType.SUB_NORMAL)
    item_1 = Tex(r"PC$_{DL}$ is a Polynomial Commitment scheme", font_size=30).move_to(3*LEFT).shift(1.5*UP)
    item_2 = create_item(Tex(r"Based on IPA [BCCGP16, Bulletproofs, Halo]", font_size=30)).next_to(item_1, DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Tex(r"Secure in DL + ROM", font_size=30)).next_to(item_2, DOWN).align_to(item_1, LEFT)
    item_4 = create_item(Tex("Uses a Uniform Reference String", font_size=30)).next_to(item_3, DOWN).align_to(item_1, LEFT)
    item_5 = create_item(Tex("Verification of evaluation proofs require $O(d)$ scalar multiplications in $\mathbb{G}$", font_size=30)).next_to(item_4, DOWN).align_to(item_1, LEFT)
    self.add(title, item_1, item_2, item_3, item_4, item_5)
    self.wait()

    self.next_section("J.2", PresentationSectionType.SUB_NORMAL)
    table = MathTable(
            [["G_0, G_1, \dots, G_d", "C \leftarrow \sum_i^d a_i G_i", "W \leftarrow IPA.Prove(C, a, z)", "IPA.Verify(C, z, v, W)"]],
            col_labels=[Text("URS", font_size=30), Text("PC.Commit(f)", font_size=30), Text("PC.Open(f, z)", font_size=30), Text("PC.Check(C, W, z, v)", font_size=30)])

    table.get_entries((2,4)).set_color(RED)
    table = table.scale(0.5).shift(2.6*DOWN)    
    self.add(table)
    self.wait()

class K_PCDL2(Scene):
  def construct(self):
    self.next_section("K", PresentationSectionType.NORMAL)
    title = Tex(r"Accumulation Scheme for PC$_{DL}$").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("K.1", PresentationSectionType.SUB_NORMAL)
    intro = Tex("Halo [BGH19] describes a protocol for accumulating PC$_{DL}$", font_size=30).move_to(2*LEFT).shift(2.1*UP)
    item_1 = create_item(Tex(r"The IPA verifier generates $O(\log d)$ challenges using the RO", font_size=27)).next_to(intro, DOWN).align_to(intro, LEFT)
    item_2 = create_item(Tex(r"Then performs cheap checks requiring $O(\log d)$ field and group operations", font_size=27)).next_to(item_1, DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Tex(r"Finally performs an expensive check (about $U$ in $\pi$) requiring $\Omega(d)$ mults", font_size=27)).next_to(item_2, DOWN).align_to(item_1, LEFT)
    self.add(item_1, item_2, item_3)
    self.wait()

    self.next_section("K.2", PresentationSectionType.SUB_NORMAL)
    item_4 = Tex(r"$U$ can be seen as a commitment to the polynomial $h = \prod_i (1 + \xi_{\log d - i}X^{2^i})$", font_size=27).next_to(item_3, DOWN).align_to(item_1, LEFT)
    item_5 = create_item(Tex(r"The AS prover creates (random) linear combinations of $U_i$", font_size=27)).next_to(item_4, DOWN).align_to(item_1, LEFT)
    item_6 = create_item(Tex(r"The AS verifier runs the fast IPA verifier; then checks $U$ is well-formed", font_size=27)).next_to(item_5, DOWN).align_to(item_1, LEFT)
    item_7 = create_item(Tex(r"The AS decider runs the (one-time) expensive check of PC.Check on U", font_size=27)).next_to(item_6, DOWN).align_to(item_1, LEFT)
    self.add(item_4, item_5, item_6, item_7)
    self.wait() 

    self.next_section("K.3", PresentationSectionType.SUB_NORMAL)
    table = MathTable(
            [["\Theta(nd) \,\mathbb{G} \mbox{ mults}", "\Theta(n \log d) \,\mathbb{G} \mbox{ mults}", "\Theta(d)\,\mathbb{G} \mbox{ mults}", "\Theta(\log d)\,\mathbb{G}"]],
            col_labels=[Text("check n evaluation proofs", font_size=30), Text("check accumulation step", font_size=30), Text("check final accumulator", font_size=30), Text("accumulator size", font_size=30)]).scale(0.5).shift(3.2*DOWN)

    table.get_entries((2,1)).set_color(RED)
    table.get_entries((2,2)).set_color(GREEN)
    table.get_entries((2,3)).set_color(RED)
    table.get_entries((2,4)).set_color(GREEN)
    
    self.add(table)
    self.wait()

class L_PCKZG(Scene):
  def construct(self):
    self.next_section("L", PresentationSectionType.NORMAL)
    title = Tex(r"PC$_{KZG}$: Overview").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("L.1", PresentationSectionType.SUB_NORMAL)
    item_1 = Tex(r"PC$_{KZG}$ is a Polynomial Commitment scheme based on Bilinear Groups", font_size=30).move_to(LEFT).shift(1.5*UP)
    item_2 = create_item(Tex(r"Based on Bilinear Groups", font_size=30)).next_to(item_1, DOWN).align_to(item_1, LEFT)
    item_3 = create_item(Tex(r"Secure in AGM + RO", font_size=30)).next_to(item_2, DOWN).align_to(item_1, LEFT)
    item_4 = create_item(Tex(r"Uses a Structured Reference String", font_size=30)).next_to(item_3, DOWN).align_to(item_1, LEFT)
    item_5 = create_item(Tex(r"Small proofs: $2 \mathbb{G}_1$ elements", font_size=30)).next_to(item_4, DOWN).align_to(item_1, LEFT)
    self.add(item_1, item_2, item_3, item_4, item_5)
    self.wait()

    self.next_section("M.2", PresentationSectionType.SUB_NORMAL)
    table = MathTable(
            [["G, sG, \dots, s^d G", "C \leftarrow f(s) G", "W \leftarrow f(s)-f(z)(s-z)^{-1} G", "e(W, (x-s)H) = e(C - vG, H)"]],
            col_labels=[Text("SRS", font_size=30), Text("PC.Commit(f)", font_size=30), Text("PC.Open(f, z)", font_size=30), Text("PC.Check(C, W, z, v)", font_size=30)])


    table.get_entries((2,1)).set_color(RED)
    table.get_entries((2,2)).set_color(GREEN)
    table.get_entries((2,4)).set_color(RED)
    table = table.scale(0.5).shift(2.6*DOWN)    
    self.add(table)
    self.wait()

class M_PCComparison(Scene):
  def construct(self):
    self.next_section("M", PresentationSectionType.NORMAL)
    title = Tex(r"Accumulation Schemes for PC$_{KZG}$").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("M.1", PresentationSectionType.SUB_NORMAL)
    intro = Tex(r"[BCMS20] describes a protocol for accumulating PC$_{KZG}$ too", font_size=30).move_to(2*LEFT).shift(1.5*UP)
    self.add(intro)
    self.wait()

    self.next_section("M.2", PresentationSectionType.SUB_NORMAL)
    table = MathTable(
            [["\Theta(n) \,\mathbb{G} \mbox{ pairings}", "\Theta(n) \,\mathbb{G}_1 \mbox{ mults}", "1\, \mbox{ pairing}", "2\,\mathbb{G}_1"]],
            col_labels=[Text("check n evaluation proofs", font_size=30), Text("check accumulation step", font_size=30), Text("check final accumulator", font_size=30), Text("accumulator size", font_size=30)]).scale(0.5)

    table.get_entries((2,1)).set_color(RED)
    table.get_entries((2,2)).set_color(ORANGE)
    table.get_entries((2,3)).set_color(RED)
    table.get_entries((2,4)).set_color(GREEN)
    
    self.add(table)
    self.wait()

class N_Results(Scene):
  def construct(self):
    self.next_section("N", PresentationSectionType.NORMAL)
    title = Text("Results").move_to(3*UP)
    self.add(title)
    self.wait()

    self.next_section("N.1", PresentationSectionType.SUB_NORMAL)
    item1 = create_item(Text("SNARKs with AS imply IVC/PCD, even without sublinear verification", font_size=20)).next_to(title, 4.5*DOWN)
    self.add(item1)
    self.wait()

    self.next_section("N.2", PresentationSectionType.SUB_NORMAL)
    item2 = create_item(Text("SNARKs with AS through PE-SNARK + accumulation scheme", font_size=20)).next_to(item1, 2.5*DOWN).align_to(item1, LEFT)
    self.add(item2)
    self.wait()

    self.next_section("N.3", PresentationSectionType.SUB_NORMAL)
    item3 = create_item(Text("Two popular polynomial commitment schemes have AS", font_size=20)).next_to(item2, 2.5*DOWN).align_to(item2, LEFT)
    self.add(item3)
    self.wait()

    self.next_section("N.4", PresentationSectionType.SUB_NORMAL)
    b1 = BraceLabel(VGroup(item1, item2), "STD", brace_direction=LEFT, color=BLUE)
    self.add(b1)
    self.wait()

    self.next_section("N.5", PresentationSectionType.SUB_NORMAL)
    b2 = BraceLabel(VGroup(item2, item3), "ROM", brace_direction=RIGHT, color=GREEN)
    self.add(b2)
    self.wait()

class O_Thanks(Scene):
  def construct(self):
    self.next_section("O", PresentationSectionType.NORMAL)
    title = Text("Thanks :)")
    self.play(Write(title))
