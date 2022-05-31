uniform float theta;
uniform vec2 offset;
uniform float scale;
uniform vec2 ratio;
attribute vec2 position;
attribute vec2 texcoord;
varying vec2   v_texcoord;
void main()
{
  v_texcoord = texcoord;
  float ct = cos(theta);
  float st = sin(theta);
  vec2 pos_ = position * ratio;
  float x = 0.75* (pos_.x*ct - pos_.y*st);
  float y = 0.75* (pos_.x*st + pos_.y*ct);
  vec2 pos = (vec2(x, y) + offset);
  gl_Position = vec4(pos.xy, 0.0, 1.0*scale);
}
