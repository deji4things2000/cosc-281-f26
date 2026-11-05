"""PS3 Task 2: select controller settings for the provided experiment.

Edit only the five tuples below. Run:
    python ps3/code/run_control.py

PID tuples are (kp, ki, kd). Useful exploration ranges are
kp: 0.2--4, ki: 0--1, kd: 0.2--4.
Start with ki=0 when studying overshoot and damping. Increasing kd often
reduces oscillation but can make the response slow. Integral action can
remove a persistent offset from the constant disturbance.

LQR tuples are (position weight, velocity weight, effort weight).
Try positive weights from 0.1--10. The provided solver computes K.
A larger velocity penalty often gives a slower, less oscillatory response.
Changing all weights by the same factor does not change the LQR policy.

These are exploration ranges, not grading bounds. Many settings pass.
The initial values below run, but do not meet every requested response.
"""

# TODO: visible overshoot followed by convergence, with no disturbance.
# kp is high relative to kd, so the response drives past the target;
# kd = 1.0 adds enough damping to settle within ~10 s without killing
# the visible overshoot.
PID_OVERSHOOT = (2.5, 0.0, 1.0)

# TODO: deliberately slow, nearly non-overshooting response, with no disturbance.
# Low kp keeps the rise slow; kd high relative to kp gives heavy damping.
PID_SLOW = (0.35, 0.0, 1.5)

# TODO: recover to the reference after the constant load begins at 8 seconds.
# ki = 0.8 accumulates the steady error caused by d = -0.2 m/s^2 and
# drives the command until the offset is cancelled. kp/kd are moderately
# damped so the integral term does not destabilize the loop.
PID_REJECT = (1.5, 0.8, 1.5)

# TODO: prompt LQR response with modest overshoot, with no disturbance.
# Large qp/q_v ratio -> fast; small r -> effort penalty is light.
LQR_RESPONSIVE = (3.0, 1.0, 0.3)

# TODO: slower LQR response with very little overshoot, with no disturbance.
# Heavy velocity penalty -> slow, smooth; effort weight keeps it gentle.
# The large q_v is what makes this at least 1.5 s slower than the
# responsive LQR.
LQR_GENTLE = (1.0, 8.0, 1.5)