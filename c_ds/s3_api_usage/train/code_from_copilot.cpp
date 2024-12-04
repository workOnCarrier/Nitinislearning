#include <aws/core/Aws.h>
#include <aws/s3/S3Client.h>
#include <aws/s3/model/PutObjectRequest.h>
#include <aws/s3/model/GetObjectRequest.h>
#include <fstream>

void UploadFileToS3(const Aws::String& bucket_name, const Aws::String& object_name, const Aws::String& file_name) {
    Aws::S3::S3Client s3_client;

    Aws::S3::Model::PutObjectRequest object_request;
    object_request.SetBucket(bucket_name);
    object_request.SetKey(object_name);

    auto input_data = Aws::MakeShared<Aws::FStream>("SampleAllocationTag",
                                                    file_name.c_str(), 
                                                    std::ios_base::in | std::ios_base::binary);

    object_request.SetBody(input_data);

    auto put_object_outcome = s3_client.PutObject(object_request);

    if (put_object_outcome.IsSuccess()) {
        std::cout << "Successfully uploaded " << object_name << " to " << bucket_name << std::endl;
    } else {
        std::cerr << "Failed to upload " << object_name << " to " << bucket_name << ": " 
                  << put_object_outcome.GetError().GetMessage() << std::endl;
    }
}

void DownloadFileFromS3(const Aws::String& bucket_name, const Aws::String& object_name, const Aws::String& file_name) {
    Aws::S3::S3Client s3_client;

    Aws::S3::Model::GetObjectRequest object_request;
    object_request.SetBucket(bucket_name);
    object_request.SetKey(object_name);

    auto get_object_outcome = s3_client.GetObject(object_request);

    if (get_object_outcome.IsSuccess()) {
        auto& retrieved_file = get_object_outcome.GetResultWithOwnership().GetBody();
        std::ofstream output_file(file_name.c_str(), std::ios::binary);
        output_file << retrieved_file.rdbuf();
        std::cout << "Successfully downloaded " << object_name << " from " << bucket_name << std::endl;
    } else {
        std::cerr << "Failed to download " << object_name << " from " << bucket_name << ": " 
                  << get_object_outcome.GetError().GetMessage() << std::endl;
    }
}

int main() {
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    {
        const Aws::String bucket_name = "your-bucket-name";
        const Aws::String object_name = "your-object-name";
        const Aws::String file_name = "your-file-name";

        UploadFileToS3(bucket_name, object_name, file_name);
        DownloadFileFromS3(bucket_name, object_name, file_name);
    }
    Aws::ShutdownAPI(options);
    return 0;
}