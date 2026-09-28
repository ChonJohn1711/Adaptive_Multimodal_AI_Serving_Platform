# Adaptive Multimodal AI Serving Platform

> **Tên đầy đủ:** A Resource-Aware and Quality-Aware Distributed Inference System for Heterogeneous AI Workloads  
> **Loại dự án:** Research-oriented, open-source engineering project  
> **Trọng tâm:** AI/ML Engineering · AI Infrastructure · Computer Vision · Distributed Systems · Cloud/SRE  
> **Thời gian dự kiến:** 9–12 tháng, có thể điều chỉnh sau giai đoạn đánh giá tính khả thi  
> **Hạ tầng:** Azure for Students (100 USD tín dụng), môi trường local và tài nguyên tính toán được cấp quyền sử dụng (nếu có)  
> **Trạng thái:** Đề xuất dự án và định hướng nghiên cứu — *chưa có kết quả thực nghiệm; chưa khẳng định tính mới khoa học*.

## 1. Tóm tắt dự án

**Adaptive Multimodal AI Serving Platform** là nền tảng tiếp nhận yêu cầu suy luận AI (*inference requests*), lựa chọn **mô hình tương thích với tác vụ** và **worker phù hợp**, sau đó điều phối thực thi theo trạng thái tải, giới hạn tài nguyên, yêu cầu chất lượng và thời gian phản hồi.

Thay vì chỉ triển khai một mô hình phía sau một REST API, dự án nghiên cứu cách vận hành **nhiều phiên bản mô hình trên các worker có cấu hình không đồng nhất** trong khi workload thay đổi theo thời gian. Đầu ra gồm hai sản phẩm có thể đánh giá độc lập:

1. **Hệ thống engineering:** inference gateway, model registry, worker management, scheduler, execution adapters, observability và bộ công cụ benchmark có thể tái lập.
2. **Đóng góp nghiên cứu dự kiến:** một chính sách *quality-aware + resource-aware model–worker scheduling*, được so sánh công bằng với các baseline dưới nhiều điều kiện tải và tài nguyên.

**Giới hạn quan trọng:** "Multimodal" là khả năng mở rộng của nền tảng, không phải yêu cầu mọi mô hình phải xử lý mọi loại dữ liệu. **Phiên bản nghiên cứu đầu tiên chỉ dùng một tác vụ thị giác với nhiều model variants có cùng input/output contract**; sau khi có benchmark đáng tin cậy mới mở rộng sang video hoặc image–text.

## 2. Bối cảnh và bài toán thực tế

Một hệ thống kiểm tra chất lượng công nghiệp có thể nhận đồng thời:

- Ảnh sản phẩm để phân loại bình thường/bất thường;
- Video ngắn để nhận diện sự kiện bất thường;
- Ảnh kèm câu hỏi để phân tích hoặc giải thích kết quả bằng mô hình thị giác–ngôn ngữ.

Các request khác nhau về kích thước, độ khó, thời hạn xử lý và yêu cầu chất lượng. Các mô hình khác nhau về accuracy, khả năng nhận diện lỗi hiếm, latency và lượng CPU/GPU/RAM sử dụng. Worker có thể chạy trên CPU, GPU hoặc các máy chủ có sức mạnh không đồng nhất.

Những chính sách đơn giản thường bỏ qua một phần của bài toán:

- **Fixed model:** dùng một mô hình cho mọi request tương thích;
- **Round-robin / shortest queue:** phân tải theo worker nhưng có thể bỏ qua sự khác biệt chất lượng giữa các mô hình;
- **Quality-only routing:** xét chất lượng ước lượng nhưng có thể đẩy request vào worker đang quá tải;
- **Resource-only routing:** xét trạng thái tài nguyên nhưng có thể chọn mô hình không đáp ứng chất lượng.

**Câu hỏi chính:** Với cùng một workload và ngân sách tài nguyên, một scheduler kết hợp ước lượng chất lượng dự đoán và trạng thái hệ thống động có cải thiện được trade-off giữa **chất lượng, p95 latency và chi phí tài nguyên** so với các chính sách chỉ xét một chiều hay không?

Một tình huống minh họa: ảnh lỗi rõ ràng có thể xử lý bằng mô hình CNN nhẹ trên CPU; ảnh có lỗi nhỏ có thể cần model variant mạnh hơn. Tuy vậy, lựa chọn cuối còn phụ thuộc vào thời gian chờ, worker availability và deadline. Các nhận định này là **giả thuyết để kiểm chứng**; hệ thống không thể biết chắc mô hình nào dự đoán đúng trước khi có ground truth.

## 3. Mục tiêu, phạm vi và ranh giới

### 3.1. Mục tiêu kỹ thuật

- Tiếp nhận và theo dõi inference requests thông qua API thống nhất.
- Đăng ký nhiều model variants và kiểm tra tương thích task/input/output.
- Thực thi trên ít nhất hai worker có cấu hình hoặc giới hạn tài nguyên khác nhau.
- Hỗ trợ các chính sách định tuyến/scheduling có thể thay thế và chạy benchmark trên cùng workload.
- Ghi nhận đầy đủ queueing, execution, network overhead, failure và tài nguyên tiêu thụ.
- Thực hành triển khai, CI/CD, quan sát và khôi phục sự cố ở môi trường Azure với chi phí kiểm soát được.

### 3.2. Mục tiêu nghiên cứu

- Xây dựng/đánh giá mô hình **ước lượng chất lượng theo request** cho các model variants tương thích.
- Xây dựng/đánh giá mô hình **ước lượng completion time** theo model–worker pair và trạng thái tải.
- Phát triển chính sách điều phối kết hợp hai ước lượng trên với constraints về tài nguyên và deadline.
- Định lượng lợi ích, overhead, giới hạn và các trường hợp thất bại bằng thí nghiệm tái lập.

### 3.3. Ngoài phạm vi của phiên bản đầu

- Tự huấn luyện foundation model hoặc tự viết inference engine thay thế vLLM/ONNX Runtime.
- Giải quyết đồng thời image classification, object detection, video understanding và VQA ngay từ đầu.
- Triển khai cụm GPU chạy liên tục 24/7 trên Azure.
- Tuyên bố bảo đảm "mỗi request đạt độ chính xác X%" khi chưa có nhãn thực tế.
- Coi demo chạy được, dashboard đẹp hoặc việc sử dụng Kubernetes là bằng chứng cho tính mới nghiên cứu.

## 4. Người dùng và cách sử dụng nền tảng

**Đối tượng:** kỹ sư ML/AI có nhiều mô hình cần serving; kỹ sư platform phụ trách tài nguyên; nhà nghiên cứu scheduling muốn kiểm tra chính sách của mình.

Một luồng sử dụng điển hình:

1. Kỹ sư đăng ký một *task contract* và hai hoặc nhiều model variants hỗ trợ contract đó.
2. Profiler đo các model variants trên worker classes và lưu latency/memory profiles.
3. Người dùng gửi inference request kèm task type, input, deadline (nếu có) và quality policy.
4. Gateway xác thực, kiểm tra schema, gán request ID và chuyển request tới scheduler.
5. Scheduler kiểm tra model compatibility, ước lượng chất lượng/completion time và chọn model–worker.
6. Worker chạy inference và trả kết quả cùng thông tin model/version và execution metadata.
7. Telemetry được ghi nhận; hệ thống benchmark đánh giá kết quả sau khi có ground truth hoặc nhãn được cung cấp riêng.

**Lưu ý:** Nếu không có model nào đáp ứng điều kiện ước lượng, hệ thống phải có trạng thái rõ ràng: từ chối, đưa vào hàng đợi, trả về kết quả có gắn uncertainty hoặc chuyển kiểm tra thủ công theo chính sách ứng dụng. Không được âm thầm chọn mô hình không tương thích.

## 5. Câu hỏi nghiên cứu và giả thuyết

| ID | Câu hỏi nghiên cứu | Giả thuyết cần kiểm chứng |
|---|---|---|
| RQ1 | Có thể dự đoán chất lượng của model variant theo request đủ tốt trước inference không? | Một quality estimator đã hiệu chuẩn giúp routing hợp lý hơn chính sách fixed-model hoặc confidence threshold đơn giản. |
| RQ2 | Có thể dự đoán thời gian hoàn thành theo model–worker–queue state không? | Mô hình dự đoán latency động giảm sai lệch so với profile tĩnh trên workload biến đổi. |
| RQ3 | Kết hợp quality-aware và resource-aware scheduling có hữu ích không? | Chính sách kết hợp cải thiện trade-off quality–latency–resource trong một số điều kiện tải so với quality-only và resource-only. |
| RQ4 | Scheduler có ổn định khi workload dịch chuyển và worker lỗi không? | Policy có thể duy trì hoạt động, và độ suy giảm có thể định lượng được dưới burst traffic, drift và worker loss. |
| RQ5 (mở rộng) | Policy học trên image workload có chuyển sang các task khác không? | Một scheduler dùng chung *có thể* tái sử dụng được khi task-specific metrics, compatibility và profiler được khai báo đúng. |

**Research gap chưa được xác nhận.** Các ý tưởng quality-aware routing, model selection, batching, heterogeneous scheduling và autoscaling đã có trong tài liệu. Cần khảo sát kỹ công trình liên quan trước khi khẳng định một thành phần cụ thể là mới.

## 6. Kiến trúc logic

```text
                    Client / Benchmark Workload Generator
                                      |
                                      v
                    +-----------------------------------+
                    | Inference Gateway                 |
                    | auth · validation · request IDs  |
                    +-----------------------------------+
                                      |
                                      v
                    +-----------------------------------+
                    | Adaptive Scheduler                |
                    | task compatibility                |
                    | quality estimator                 |
                    | latency / queue estimator         |
                    | model–worker assignment           |
                    +-----------------------------------+
                       |                  |           |
              +--------+-----+     +------+-----+     |
              | Model Registry|     | Worker State|   |
              | version/task  |     | heartbeat   |   |
              | profiles      |     | capacity    |   |
              +--------------+     +------------+    |
                                                        v
                           +----------------------------------------+
                           | Queue / Dispatch Layer                 |
                           +----------------------------------------+
                              |                    |               |
                              v                    v               v
                        CPU Worker A         CPU Worker B     GPU Worker C*
                        Model A              Model A/B       Model B/VLM*
                              \                    |              /
                               +--------- Result Collector --------+
                                             |
                                             v
                               Response + Execution Metadata

      Telemetry / Tracing / Benchmark Store: xuyên suốt mọi thành phần

      *GPU worker/VLM là phần mở rộng, không bắt buộc trong MVP.
```

### 6.1. Các thành phần và trách nhiệm

| Thành phần | Trách nhiệm | Tự phát triển hay tận dụng |
|---|---|---|
| Inference Gateway | API, authentication, schema, timeout, request ID | Tự phát triển trên FastAPI/Go; tận dụng server/framework |
| Model Registry | Phiên bản, task contract, artifact URI, performance profile | Tự xây lớp metadata, dùng object storage/DB hiện có |
| Quality Estimator | Ước lượng chất lượng theo request và model | Tự thiết kế, huấn luyện/hiệu chuẩn/đánh giá |
| Latency Estimator | Ước lượng queueing + execution + network | Tự xây/kiểm chứng, dùng profile và telemetry |
| Adaptive Scheduler | Chọn model–worker, constraints, fallback | **Đóng góp nghiên cứu chính dự kiến** |
| Dispatcher / Queue | Chuyển request, timeout, retry và trạng thái | Dùng queue/framework phù hợp, tự xây state handling cần thiết |
| Inference Workers | Model loading, inference, result, health | Tự xây adapter; dùng PyTorch/ONNX Runtime hoặc serving engine |
| Observability | Metrics, logs, traces, request lifecycle | OpenTelemetry/Prometheus/Grafana hoặc Azure Monitor |
| Benchmark Suite | Workload, baseline, fault injection, phân tích | Tự phát triển để bảo đảm tái lập |

### 6.2. Hợp đồng dữ liệu tối thiểu

**Request metadata:** `request_id`, `task_type`, `input_uri` hoặc payload, `input_schema_version`, `deadline_ms` (tùy chọn), `quality_policy`, `submitted_at`.

**Model metadata:** `model_id`, `version`, `supported_task_types`, `input_schema`, `output_schema`, `runtime`, `supported_hardware`, `artifact_hash`, performance profile và calibration metadata.

**Worker metadata:** `worker_id`, `hardware_class`, `models_loaded`, `available_memory`, `active_requests`, `queue_depth`, `last_heartbeat`, `health_status`.

**Result metadata:** `request_id`, `model_id`, `model_version`, `worker_id`, `status`, `prediction`, `uncertainty` (nếu có), `queue_ms`, `execution_ms`, `network_ms`, `end_to_end_ms`.

Mọi dữ liệu đo chất lượng offline phải gắn với **dataset/version/split** và nhãn; không trộn nhãn thật vào dữ liệu mà online scheduler được phép xem.

## 7. Định nghĩa bài toán scheduling

Với request \(x_i\), gọi \(\mathcal{M}(x_i)\) là các mô hình **tương thích task và schema**; \(\mathcal{W}(m)\) là các worker đủ khả năng chạy mô hình \(m\). Scheduler lựa chọn:

```math
a_i=(m_i,w_i,b_i),\quad m_i\in\mathcal{M}(x_i),\quad w_i\in\mathcal{W}(m_i)
```

Trong đó \(b_i\) là phương án batch hoặc execution slot (có thể bỏ qua ở phiên bản đầu).

Một phát biểu nghiên cứu ban đầu:

```math
\min_{m,w}\ \widehat{T}_{\mathrm{completion}}(x_i,m,w)
```

với các ràng buộc về compatibility, RAM/VRAM, deadline và **quality risk** đã định nghĩa trên một tập workload/nhóm dữ liệu phù hợp.

Một số lượng cần ước lượng:

- \(\widehat{Q}(x,m)\): khả năng mô hình \(m\) đạt tiêu chí chất lượng trên \(x\), hoặc một score có hiệu chuẩn được; **không phải ground-truth accuracy biết trước**.
- \(\widehat{T}(x,m,w)\): queueing + model execution + network/serialization + routing overhead.
- \(\widehat{C}(x,m,w)\): CPU/GPU-seconds, memory-time hoặc monetary cost theo cách đo đã công bố.

Không nên cộng trực tiếp accuracy, latency và USD vào một tổng điểm khi chưa chuẩn hóa/giải thích trọng số. Hướng đánh giá rõ ràng hơn là so sánh **Pareto trade-off** hoặc tối thiểu hóa latency/resource *tại cùng một ngưỡng chất lượng thực nghiệm*.

### 7.1. Điểm khó mang tính nghiên cứu

- **Quality estimation:** Mô hình có thể tự tin cao nhưng sai; kiểm tra calibration, OOD và nhóm lỗi hiếm.
- **Dynamic latency:** Profile tĩnh không phản ánh queueing, batch, đồng thời và mạng.
- **Heterogeneous hardware:** Cùng model có latency/memory khác nhau giữa các worker.
- **Decision overhead:** Router phức tạp có thể triệt tiêu lợi ích của việc chọn model nhẹ.
- **Constraint infeasibility:** Không có phương án vừa đạt quality estimate, deadline vừa vừa tài nguyên.
- **Failure semantics:** Worker timeout không chứng minh request chưa được thực thi; retry cần request tracking/deduplication và giới hạn số lần.

## 8. Phạm vi phiên bản đầu và mở rộng multimodal

### Giai đoạn đầu — Visual inference (bắt buộc)

- **Task:** binary image anomaly classification hoặc một tác vụ phân loại thị giác có nhãn đáng tin cậy.
- **Models:** ít nhất hai model variants có cùng output schema; một mô hình nhẹ và một mô hình nặng hơn.
- **Workers:** ít nhất hai worker classes hoặc hai giới hạn tài nguyên đo được (ví dụ: CPU máy cá nhân và CPU VM nhỏ; GPU chỉ khi có sẵn).
- **Policies:** fixed-small, fixed-large, round-robin/shortest-queue khi phù hợp, quality-only, resource-only và proposed joint policy.
- **Đánh giá:** quality trên holdout, p50/p95/p99 latency, throughput, resource/request, failure/deadline misses và scheduling overhead.

### Mở rộng — Video inference (sau khi hệ thống đầu ổn định)

Thêm một *task contract* riêng cho video anomaly detection, hỗ trợ metadata về clip duration, frame sampling và timestamp. Không dùng accuracy của image classification để so sánh trực tiếp với video detection. Cần xử lý đúng việc chia clip và hợp nhất kết quả theo timeline nếu có video chunking.

### Mở rộng — Image + text / LLM serving (tùy tài nguyên)

Thêm VQA hoặc một tác vụ image-text xác định. Với LLM/VLM, bộ đo cần bổ sung token throughput, time to first token, time per output token và memory/KV cache khi phù hợp. Phạm vi này **không bắt buộc** để hoàn thành đóng góp nghiên cứu đầu tiên.

## 9. Thiết kế thực nghiệm

### 9.1. Nguyên tắc

- Dùng cùng dataset split, request trace, model weights, cấu hình phần cứng và điều kiện tài nguyên cho các baseline có thể so sánh.
- Khóa các phiên bản thư viện, lưu seed và toàn bộ config; lặp lại thí nghiệm để đo độ biến thiên.
- Tách **training/calibration/validation/test** của quality estimator; không leakage từ test labels vào routing.
- Báo cáo chi phí router, timeouts, dropped requests và các trường hợp không thỏa constraints — không chỉ báo cáo các request thành công.
- Phân biệt kết quả **mô phỏng**, **local physical cluster** và **Azure deployment**.

### 9.2. Các workload scenarios

| Scenario | Cần kiểm tra |
|---|---|
| Steady arrival | Hiệu quả khi tải ổn định |
| Bursty traffic | Queueing, p95/p99 latency và sự ổn định chính sách |
| Mixed easy/hard inputs | Trade-off giữa chất lượng và tài nguyên |
| Distribution shift / OOD | Độ bền của quality estimator và routing |
| Worker loss / timeout | Request recovery, deduplication và thời gian phục hồi |
| Heterogeneous workers | Lợi ích/hạn chế của resource-aware placement |
| Cold model / model loading | Overhead thay model hoặc khởi động worker |

### 9.3. Baseline và ablation

**Baselines:** fixed-small; fixed-large; round-robin; shortest-queue; quality-only; resource-only; một phương pháp liên quan đã công bố **nếu triển khai và tái lập được một cách công bằng**.

**Ablation:** tắt quality estimator; tắt latency predictor; dùng profile tĩnh; bỏ queue state; thay quality estimator bằng confidence threshold; bật/tắt batching (khi đã hỗ trợ).

### 9.4. Metrics

| Nhóm | Metrics | Ghi chú |
|---|---|---|
| Task quality | Accuracy/F1/AUROC, recall lỗi, false negative rate | Định nghĩa positive class và chọn metric theo mục tiêu ứng dụng |
| Latency | p50/p95/p99 end-to-end; queue/execution breakdown | Bao gồm routing, network và lỗi timeout |
| Throughput | Completed requests/second | Đo theo workload và ngưỡng chất lượng xác định |
| Resource | CPU/GPU-seconds/request; peak RAM/VRAM; utilization | Công bố cách lấy mẫu/đo |
| Reliability | Error rate, deadline-miss rate, recovery time | Phân biệt lỗi do mô hình, worker và mạng |
| Router quality | Prediction calibration, routing regret (nếu định nghĩa được), overhead | Không coi confidence là xác suất đúng khi chưa kiểm chứng |
| Cost | Chi phí hạ tầng/1.000 requests trong điều kiện đo | Chỉ báo cáo USD nếu có billing hoặc mô hình chi phí minh bạch |

**Tiêu chí thành công nghiên cứu:** chứng minh được một cải thiện có ý nghĩa trong một miền workload và constraints cụ thể, kèm phân tích khi nào policy thất bại. Không đặt trước tỷ lệ cải thiện chưa được đo.

## 10. Azure: vai trò và giới hạn ngân sách

Azure là **môi trường triển khai và kiểm chứng hệ thống**, không nhất thiết là nơi chạy tất cả thí nghiệm AI liên tục.

| Nhu cầu | Dịch vụ/giải pháp cân nhắc | Ghi chú chi phí |
|---|---|---|
| Gateway, scheduler, worker nhỏ | Azure Container Apps | Kiểm tra region, quota, consumption plan và tài nguyên phụ trợ |
| VM Linux phục vụ benchmark ngắn hạn | Azure Virtual Machines | Trả phí theo SKU/thời gian và một số tài nguyên đi kèm; xóa tài nguyên sau thử nghiệm |
| Model artifacts, traces, dữ liệu thí nghiệm | Azure Blob Storage | Storage, transactions và egress có thể phát sinh phí |
| Telemetry | Azure Monitor hoặc stack Prometheus/Grafana tự triển khai | Giới hạn log ingestion, retention và dịch vụ liên quan |
| CI/CD | GitHub Actions | Kiểm tra quota Actions và build minutes |
| Infrastructure as Code | Terraform hoặc Bicep | Chỉ thực thi `apply/deploy` trong cửa sổ thực nghiệm được kiểm soát |

**Quy tắc quản lý 100 USD tín dụng:**

1. Thiết lập budget alerts; nhớ rằng **cảnh báo không phải hard spending cap**.
2. Dùng local + Docker + simulation cho phần lớn phát triển và baseline.
3. Chỉ khởi tạo Azure resources khi có experiment được xác định trước; ghi lại giờ bắt đầu/kết thúc và chi phí.
4. Ưu tiên các phiên benchmark ngắn với CPU worker; GPU Azure không được giả định là có quota hoặc nằm trong ngân sách.
5. Dọn resource group, VM, managed disks, public IP, logs và các tài nguyên còn tính phí sau thí nghiệm; kiểm tra billing sau đó.
6. Không cam kết một mức chi phí cụ thể khi chưa chọn region, SKU, retention, lưu lượng và thời gian hoạt động.

Mọi quyền truy cập từ worker ngoài Azure phải được xác thực/bảo vệ; không mở cổng SSH, Redis hay model-serving nội bộ công khai không kiểm soát.

## 11. Công nghệ đề xuất và tiêu chí lựa chọn

- **Backend/control plane:** Python + FastAPI để phát triển nhanh; cân nhắc Go cho thành phần yêu cầu concurrency cao sau khi đo bottleneck.
- **Model runtime:** PyTorch hoặc ONNX Runtime cho visual MVP. Ray Serve/vLLM chỉ thêm nếu đáp ứng đúng nhu cầu; không tự viết lại các engine sẵn có.
- **Metadata/state:** PostgreSQL hoặc giải pháp nhẹ trong prototype; phân biệt state bền vững và telemetry tạm thời.
- **Queue/dispatch:** Redis Streams, RabbitMQ hoặc framework có semantics phù hợp với retry và acknowledgement; chọn sau khi rõ delivery semantics.
- **Observability:** OpenTelemetry, Prometheus/Grafana và/hoặc Azure Monitor.
- **Packaging/deployment:** Docker, GitHub Actions, Terraform/Bicep; Kubernetes là tùy chọn nghiên cứu, không phải điều kiện hoàn thành.
- **Benchmark:** workload generator có seed/trace cố định, runner cho baseline và script tổng hợp thống kê.

**Nguyên tắc:** Chọn công nghệ theo yêu cầu và benchmark, không lấy số lượng công nghệ làm chỉ số chất lượng dự án.

## 12. Lộ trình 9–12 tháng và điều kiện chuyển giai đoạn

| Giai đoạn | Mục tiêu | Đầu ra/điều kiện hoàn thành |
|---|---|---|
| Tháng 1–2 | Literature review, chọn task/dataset/models, thiết lập baseline | Problem statement, related-work matrix, dataset splits, baseline report |
| Tháng 3–4 | Gateway + registry + multi-worker serving + telemetry | Chạy được cùng một request trace trên ít nhất hai worker; có logs/metrics đầy đủ |
| Tháng 5–6 | Quality/latency estimator và scheduler thử nghiệm | So sánh quality-only, resource-only, joint policy; báo cáo failure cases và overhead |
| Tháng 7–8 | Reliability, CI/CD và Azure deployment có kiểm soát | Reproducible deploy, benchmark thực tế trên Azure, fault-injection report |
| Tháng 9–10 | Mở rộng workload hoặc cải thiện policy theo kết quả | Ablations, stress tests; chỉ thêm video/image-text nếu kết quả visual MVP vững |
| Tháng 11–12 | Đóng gói open-source và research report | README, architecture/design decisions, benchmark scripts, configs, technical report/paper draft nếu đủ đóng góp |

**Điểm dừng có chủ đích:** Nếu đến tháng 6 chưa có cải thiện hoặc estimators không đủ tin cậy, tập trung phân tích nguyên nhân và hoàn thiện benchmark/engineering system; không mở rộng sang nhiều modalities chỉ để tăng độ lớn dự án.

## 13. Deliverables cho portfolio và nghiên cứu

### Engineering deliverables

- Public GitHub repository với license, hướng dẫn chạy local, cấu trúc rõ ràng và mẫu cấu hình không chứa secrets.
- Architecture document, task/model/worker contracts và sơ đồ request lifecycle.
- Unit/integration/load tests; test tình huống worker crash, timeout, duplicate request.
- Docker-based reproduction và IaC/deployment configs cho Azure.
- Dashboard/trace ví dụ và tài liệu vận hành: deploy, rollback, cleanup, cost control.
- Benchmark suite với dữ liệu/trace hợp lệ, baseline policies và report generator.

### Research deliverables

- Literature review và bảng so sánh giới hạn phương pháp liên quan.
- Định nghĩa RQ, giả thuyết, policy, assumptions và phạm vi áp dụng.
- Tập dữ liệu/splits/weights/configs có nguồn gốc và quyền sử dụng rõ ràng.
- Bảng kết quả quality–latency–resource với số lần lặp và độ biến thiên.
- Ablation studies, sensitivity analyses, failure cases và threats to validity.
- Technical report; chỉ chuẩn bị bản thảo công bố khi có đóng góp và bằng chứng thực nghiệm phù hợp.

## 14. Rủi ro và cách giảm thiểu

| Rủi ro | Tác động | Cách xử lý |
|---|---|---|
| Quality estimator không chính xác trên ảnh khó/OOD | Routing chọn model không phù hợp | Calibration, OOD tests, conservative fallback, phân tích false negatives |
| Router overhead lớn hơn lợi ích | Latency tăng | Đo overhead end-to-end, tối giản đặc trưng và thử policy đơn giản |
| Tài nguyên Azure hết nhanh | Không đủ ngân sách benchmark | Local/simulation first, benchmark ngắn, budget alerts và cleanup |
| Không có GPU quota | Không đo được GPU-heavy workloads trên Azure | CPU-first scope, GPU ngoài Azure khi có quyền, báo cáo giới hạn rõ ràng |
| Scope creep sang nhiều modalities | Khó hoàn thành/nhiễu đánh giá | Khóa visual MVP và một đóng góp nghiên cứu trước khi mở rộng |
| Benchmark thiếu công bằng hoặc data leakage | Kết luận không đáng tin cậy | Fixed traces/splits/hardware, tách dữ liệu training–test, lặp thí nghiệm |
| Retry/worker loss làm trùng kết quả | Lỗi trạng thái và sai kết quả đo | Request IDs, acknowledgement policy, idempotent result recording |
| Công trình liên quan đã giải quyết cùng bài toán | Đóng góp mới không rõ | Khảo sát sâu, định nghĩa rõ điều kiện và baseline trước khi chốt claim |

## 15. Các quyết định còn mở trước khi khởi động

1. **Tác vụ visual MVP:** binary industrial anomaly classification hay một tác vụ khác có nhãn và metric rõ ràng?
2. **Dataset:** nguồn công khai nào được phép sử dụng, đủ độ khó và có dữ liệu holdout?
3. **Model variants:** chọn cặp mô hình có trade-off chất lượng–latency đã đo được trên phần cứng thực tế.
4. **Hardware:** máy local và tài nguyên được cấp quyền sử dụng có CPU/GPU/RAM thế nào? Azure sẽ cung cấp worker class nào trong những đợt benchmark?
5. **Quality policy:** ngưỡng chất lượng được đặt theo toàn workload, nhóm dữ liệu hay rủi ro false negative?
6. **Research core:** bắt đầu từ joint quality–resource scheduling; chỉ thêm batching/autoscaling nếu thí nghiệm chỉ ra đó là bottleneck cần giải quyết.
7. **Tính mới:** sau literature review, xác định chính xác baseline khoa học và điều kiện mà phương pháp đề xuất muốn cải thiện.

## 16. Tài liệu tham khảo khởi đầu

> Các nguồn dưới đây dùng để đọc và đối chiếu. Chúng **không** chứng minh dự án đề xuất là mới; cần tiếp tục cập nhật literature review trước khi phát biểu research gap.

- **INFaaS: Automated Model-less Inference Serving** (USENIX ATC 2021): https://www.usenix.org/conference/atc21/presentation/romero
- **RouteLLM: Learning to Route LLMs with Preference Data**: https://arxiv.org/abs/2406.18665
- **Ray Serve documentation:** https://docs.ray.io/en/latest/serve/
- **vLLM / PagedAttention paper:** https://arxiv.org/abs/2309.06180
- **Azure for Students:** https://azure.microsoft.com/en-us/free/students/
- **Azure Container Apps pricing:** https://azure.microsoft.com/en-us/pricing/details/container-apps/
- **Azure pricing calculator:** https://azure.microsoft.com/en-us/pricing/calculator/

---

**Tuyên bố phạm vi:** Đây là tài liệu định nghĩa dự án ở giai đoạn đề xuất. Tên thuật toán, chỉ số cải thiện, novelty claim, chi phí vận hành và kết quả benchmark chỉ được chốt sau khi khảo sát công trình liên quan và thực nghiệm có thể tái lập.
