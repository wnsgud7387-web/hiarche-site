-- ============================================================================
-- LQ 익명 기록 — 한국어판 만 14세 이상 반영 (보완 SQL, supabase_setup.sql d5cc5a9d 다음에 실행)
-- 대표 지시 ceo-20261020-lq-age14 · 비서 작성 2026-10-20
-- 사용법: Supabase 'SQL Editor' → 새 쿼리 → 이 파일 전체 붙여 넣고 'Run' 한 번. 여러 번 실행해도 같은 결과.
-- 바뀌는 것
--  1) 나이대에 'u19'(한 14~18) 추가. 'u30'은 한 19~29 · 영 18~29 그대로
--  2) 동의 문구 판(consent_v)에 꼬리 허용: 'ko-20261020-a14'처럼 — 19세판과 14세판 동의를 구분
-- 그대로인 것: 익명은 넣기만 · 읽기·고치기·지우기 불가 · 권한·하루 상한·RLS 변경 없음
-- ============================================================================
begin;

alter table public.lq_records drop constraint if exists lq_age_ck;
alter table public.lq_records add  constraint lq_age_ck
  check (age_band is null or age_band in ('u19','u30','30s','40s','50s','60+','na'));

alter table public.lq_records drop constraint if exists lq_consent_v_ck;
alter table public.lq_records add  constraint lq_consent_v_ck
  check (consent_v ~ '^(ko|en)-[0-9]{8}(-[a-z0-9]{1,8})?$');

commit;
