import vidtoolz
import vidtoolz_trim as vt


def create_parser(subparser):
    parser = subparser.add_parser("split", description="Split a video into two")
    parser.add_argument("input", type=str, help="Single file name")
    parser.add_argument(
        "splitat",
        type=float,
        help="Split at seconds.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file (default: %(default)s)",
        default=None,
    )
    return parser


class ViztoolzPlugin:
    """Split a video into two"""

    __name__ = "split"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        output = vt.determine_output_path(args.input, args.output)
        part1 = f"{output}-part1.mp4"
        vt.trim_video(args.input, part1, 0.0, args.splitat)
        part2 = f"{output}-part2.mp4"
        vt.trim_video(args.input, part2, args.splitat, -1)

    def hello(self, args):
        # this routine will be called when "vidtoolz "split is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


split_plugin = ViztoolzPlugin()
